# V1.0 - Code

This folder contains the software source code for the first working AquaSense V1.0 prototype.

## Project Components

The V1.0 software is divided into three parts:

### Arduino

Contains the Arduino firmware responsible for:

- Reading sensor data
- Processing sensor measurements
- Displaying readings on the OLED
- Sending sensor data through serial communication

See:

`Arduino/`

### Python

Contains the Python program responsible for:

- Receiving sensor data from the Arduino through serial communication
- Processing the received data
- Sending measurements to ThingSpeak

See:

`Python/`

### Android App

Contains the Android application developed as part of the AquaSense V1.0 software implementation.

See:

`Android App/`

## V1.0 Software Flow

```text
Sensors
   ↓
Arduino
   ↓
Serial Communication
   ↓
Python
   ↓
ThingSpeak
