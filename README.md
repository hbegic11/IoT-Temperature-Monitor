# IoT-Temperature-Monitor
An Arduino &amp; Python-based system for real-time temperature tracking. Features local LED/Buzzer alerts and a Telegram bot for remote monitoring via /temp commands and automated push notifications. Built with python-telegram-bot (JobQueue) and Serial communication.


# 🌡️ IoT Temperature Monitor (Arduino + Telegram)

This project enables real-time remote temperature monitoring using an **Arduino Uno**, **LM35 sensor**, and a **Telegram bot**. The system features a local hardware alarm (LEDs and Buzzer) and automated mobile notifications.

## 🚀 Key Features
* **Real-time Data Acquisition:** The sensor transmits data to a Python application via Serial communication every second.
* **Local Alert System:** * 🟢 Green LED: Temperature is within safe limits (< 25°C).
    * 🔴 Red LED + 🔊 Buzzer: Alarm triggers immediately if the threshold is exceeded.
* **Telegram Integration:**
    * `/temp` - Command to check current temperature status at any time.
    * **Automated Alerts:** The bot sends a push notification once overheating is detected (with built-in spam protection).

## 🛠️ Hardware Requirements
* Arduino Uno Board
* LM35 Temperature Sensor
* 2x LEDs (Red and Green)
* 1x Active Buzzer
* Resistors (220 ohm) and Jumper wires

## 📂 Project Structure
* `arduino_kod.ino` - Arduino firmware (C++).
* `bot.py` - Python Gateway and Telegram bot logic.
* `requirements.txt` - List of required Python libraries.

## ⚙️ Setup & Installation

### 1. Hardware & Arduino
1. Connect the components (LM35 to A0, LEDs to pins 8 & 9, Buzzer to pin 10).
2. Upload `arduino_kod.ino` to your board via Arduino IDE.

### 2. Python Environment
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
2. Open bot.py and enter your Telegram Bot Token and Chat ID.
3. Run the application:
  Bash
    python bot.py
