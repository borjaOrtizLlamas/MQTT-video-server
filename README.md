
      
# Code: 

**Tested on macOS Ventura 13.4**

## Overview:
This project gives you the support to create a video with your camara and save it in the server, it uses MQTT broker. 

## Components:
(server part)
1. **Broker (Mosquitto):**
   The broker component utilizes Mosquitto, an open-source message broker that implements the MQTT protocol. MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol ideal for small, efficient IoT devices.

2. **Consumer (Python Server in `./topic`):**
   This component is a Python server designed to consume messages from the broker. It likely subscribes to specific topics and processes incoming data accordingly. The Python server is located within the `./topic` directory.

(client)
3. **Client:**
   The client interacts with the broker to send data. It's a vital part of the system, responsible for initiating communication and transmitting data to the broker for further processing.

## Getting Started:
To run the project, follow these steps:

1. Execute the following command to build and launch the components using Docker Compose:

$ docker-compose up --build


2. Once the components are up and running, start the client by running the following command:

$ python3 client.py


## Data Checking:
After running the client, you should find the transmitted data stored within the `./data/` folder. This folder serves as a convenient location to inspect the data sent during the execution of the project.
