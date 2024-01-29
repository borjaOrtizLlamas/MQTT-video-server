import cv2 as cv
import paho.mqtt.client as mqtt
import base64
import time
import socket
import json

MQTT_BROKER = "127.0.0.1"
MQTT_SEND = "test-borja"
MQTT_PORT = 1885

# Obtener el nombre de la máquina
hostname = socket.gethostname()

# Capturar video desde la cámara
cap = cv.VideoCapture(0)

# Inicializar cliente MQTT
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)

try:
    while True:
        start = time.time()
        # Leer frame desde la cámara
        ret, frame = cap.read()
        if not ret:
            break
        # Codificar el frame en JPEG
        _, buffer = cv.imencode('.jpg', frame)
        # Convertir a bytes
        jpg_as_text = base64.b64encode(buffer)
        # Crear un diccionario con el nombre de la máquina y el frame codificado
        data = {'hostname': hostname, 'frame': jpg_as_text.decode('utf-8')}
        # Convertir a JSON
        json_data = json.dumps(data)
        # Publicar el frame en el topic MQTT
        client.publish(MQTT_SEND, json_data)
        end = time.time()
        t = end - start
        fps = 1 / t
        print(fps)
except KeyboardInterrupt:
    pass
finally:
    cap.release()
    client.disconnect()
    print("\nCliente desconectado y cámara liberada")
