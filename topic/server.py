
import base64
import cv2
import numpy as np
import paho.mqtt.client as mqtt
import os
import json

MQTT_BROKER = os.getenv("MQTT_BROKER", "mosquitto")
MQTT_RECEIVE = os.getenv("MQTT_RECEIVE", "test-borja")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1885))
frame = np.zeros((240, 320, 3), np.uint8)
video_started = False
video_writer = None

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_RECEIVE)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global frame, video_started, video_writer
    
    json_data = json.loads(msg.payload)
    hostname = json_data['hostname']
    img = base64.b64decode(json_data['frame'])
    npimg = np.frombuffer(img, dtype=np.uint8)
    frame = cv2.imdecode(npimg, 1)

    if not video_started:
        height, width, _ = frame.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        print("Connected with result code "+str(frame.shape))
        fps = 30
        video_writer = cv2.VideoWriter(f'/app/data/{hostname}_output.avi', fourcc, fps, (width, height))

        video_started = True
    
    video_writer.write(frame)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT)

# Starting thread which will receive the frames
client.loop_forever()

