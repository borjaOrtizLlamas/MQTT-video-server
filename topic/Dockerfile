FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 1883
WORKDIR /app
COPY server.py /app
COPY requirements.txt /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ENV MQTT_BROKER=mosquitto
ENV MQTT_RECEIVE=test-borja
ENV MQTT_PORT=1885

CMD ["python3", "server.py"]
