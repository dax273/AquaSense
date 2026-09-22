import serial
import requests
import time

# ---------------- SERIAL ----------------
ser = serial.Serial('COM4', 9600, timeout=2)
time.sleep(2)
ser.reset_input_buffer()

# ---------------- THINGSPEAK ----------------
THINGSPEAK_API_KEY = "XXXXXXXXXXXXXXXXX"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def safe_get(url, params):
    try:
        return requests.get(url, params=params, timeout=5)
    except:
        return None

print("SYSTEM STARTED")

while True:
    try:
        line = ser.readline().decode(errors='ignore').strip()

        if not line:
            continue

        print("RAW:", line)

        if line.count(",") != 3:
            print("SKIPPED BAD PACKET")
            continue

        humidity, temp, depth, tds = map(float, line.split(","))

        # ---------------- THINGSPEAK ----------------
        safe_get(THINGSPEAK_URL, {
            "api_key": THINGSPEAK_API_KEY,
            "field1": tds,
            "field2": depth,
            "field3": humidity,
            "field4": temp
        })

        print(f"D={depth} H={humidity} T={temp} TDS={tds}")

    except Exception as e:
        print("ERROR:", e)
        time.sleep(2)