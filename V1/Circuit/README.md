# v1.0 Circuit Diagram

This folder contains the circuit and wiring information for the first working AquaSense prototype.

## Components

- Arduino Uno
- TDS sensor
- 3-pin DHT22 temperature and humidity module
- HC-SR04 ultrasonic sensor
- 0.96" I2C OLED display

## Pin Configuration

| Component | Arduino Pin |
|---|---|
| DHT22 DATA | D2 |
| Ultrasonic TRIG | D4 |
| Ultrasonic ECHO | D3 |
| TDS Sensor | A0 |
| OLED SDA | A4 |
| OLED SCL | A5 |

## Circuit Diagram

The complete V1 wiring diagram is shown below.

![AquaSense V1 Circuit Diagram](Circuit%20Diagram.png)

## Power Connections

- Sensor VCC → Arduino 5V
- Sensor GND → Arduino GND
- OLED VCC → Arduino 5V
- OLED GND → Arduino GND

## Notes

The DHT22 used in V1 is a 3-pin module.

The OLED display communicates with the Arduino Uno using the I2C interface:

- SDA → A4
- SCL → A5
