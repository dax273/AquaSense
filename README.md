# AquaSense

### Low-Cost Open-Source Water Monitoring System

AquaSense is an open-source project focused on developing an affordable and accessible system for monitoring basic water and environmental parameters.

The project is being developed through multiple hardware and software iterations, with each version improving the system based on testing, observations, and practical requirements.

---

## Project Goal

The goal of AquaSense is to explore how **low-cost electronics, sensors, mobile devices, and cloud technologies** can be combined to create a practical water-monitoring system.

The project focuses on:

* Affordable hardware
* Reproducible design
* Practical environmental monitoring
* Mobile-based data access
* Offline and cloud data handling
* Open-source development
* Iterative hardware and software development

---

## How AquaSense Works

At its core, AquaSense collects measurements from sensors placed in or around a water body and processes the data using a microcontroller.

The architecture has evolved over the different versions of the project.

```text
 Water Body
     ↓
  Sensors
     ↓
Microcontroller
     ↓
Data Processing
     ↓
User Interface / Gateway
     ↓
Cloud Storage
```

---

# Project Versions

AquaSense is being developed incrementally. Each major version represents a different stage of the system.

## V1.0 — First Working Prototype

The first working AquaSense prototype was built around an Arduino-based system.

### V1 Hardware

* Arduino
* TDS sensor
* DHT22 temperature and humidity sensor
* Ultrasonic sensor
* OLED display

### V1 Capabilities

* TDS measurement
* Ambient temperature and humidity measurement
* Distance / water-level-related measurement
* Local display of sensor readings
* Initial cloud-based visualization using ThingSpeak

V1 served as the foundation for the project's later development.

**Release:** [`v1.0.0`](../../releases/tag/v1.0.0)

---

## V2.0 — Lake Monitoring Architecture

V2 focuses more specifically on water monitoring and improves the connectivity and data architecture.

### V2 Hardware

* ESP32
* TDS sensor
* Turbidity sensor
* DS18B20 waterproof temperature sensor

### V2 Architecture

```text
Lake
  ↓
TDS + Turbidity + DS18B20
  ↓
ESP32
  ↓ BLE
Android Device
  ├── BLE Gateway
  ├── Local Storage
  ├── Analytics
  └── Graphs / Dashboard
       ↓ Internet
 Supabase
  └── Historical Data
```

The Android device acts as the gateway between the ESP32 sensing node and the cloud.

This approach also allows an existing or refurbished Android device to potentially be reused instead of requiring a dedicated gateway device.

> V2 is currently under development / testing.

---

# 🔬 Sensors

The sensor configuration changes between project versions.

| Version | Controller | Sensors                 | Display / Gateway  |
| ------- | ---------- | ----------------------- | ------------------ |
| V1      | Arduino    | TDS, DHT22, Ultrasonic  | OLED + ThingSpeak  |
| V2      | ESP32      | TDS, Turbidity, DS18B20 | Android + Supabase |

---

# 🛠️ Development Approach

AquaSense follows an iterative development process:

```text
Problem
  ↓
Research
  ↓
Prototype
  ↓
Testing
  ↓
Identify Limitations
  ↓
Redesign
  ↓
Improved Version
```

Rather than treating the first prototype as the final system, each version is used to identify practical limitations and guide the next iteration.

---

# Design Principles

### Affordability

The system is designed around readily available, low-cost components wherever practical.

### Reproducibility

Hardware, firmware, documentation, and design decisions are being documented so that others can reproduce and extend the project.

### Hardware Reuse

The V2 architecture explores the use of existing or refurbished Android devices as gateways, reducing the need for a separate dedicated gateway device.

### Practicality

The project focuses on measurements and features that can realistically be implemented within the project's cost and hardware constraints.

### Open Development

The project is being documented publicly so that the development process and lessons learned can be followed across versions.

---

# Repository Structure

```text
AquaSense/
│
├── firmware/
│   ├── V1/
│   └── V2/
│
├── hardware/
│   ├── V1/
│   └── V2/
│
├── documentation/
│   ├── V1/
│   └── V2/
│
├── app/
│
├── README.md
│
└── LICENSE
```

The exact repository structure may evolve as development continues.

---

# Current Status

| Version | Status                    |
| ------- | ------------------------- |
| V1.0    | ✅ First working prototype |
| V2.0    | 🔧 Development / testing  |

---

# Releases

Major project milestones are published as GitHub releases.

* **v1.0.0** — AquaSense V1.0: First Working Prototype
* **v2.0.0** — AquaSense V2.0: Lake Monitoring Architecture *(future release)*

---

# Open Source

AquaSense is being developed as an open-source project.

The repository will progressively include:

* Firmware
* Hardware documentation
* Circuit diagrams
* Bill of Materials (BOM)
* Sensor information
* Android application
* Database structure
* Communication protocols
* Setup instructions
* Calibration information
* Development documentation

---

# Project

**AquaSense**

A student-led project exploring affordable and accessible approaches to water monitoring through embedded systems, mobile technology, and cloud-based data management.

---

## License

This project is open source. See the `LICENSE` file for details.
