# 💡 Raspberry Pi LED Control

Control an LED using Raspberry Pi GPIO pins with Python. This beginner-friendly project demonstrates basic hardware interfacing and GPIO programming.

---

## 📌 Features

- Blink an LED using Raspberry Pi
- Clean and structured Python code
- Beginner-friendly project
- Safe GPIO handling with cleanup

---

## 🛠️ Hardware Required

- Raspberry Pi (any model with GPIO)
- LED (any color)
- Breadboard
- Jumper wires
- Resistor (220Ω–330Ω recommended)

---

## 🔌 Circuit Connections

| Component | Connection |
|----------|-----------|
| GPIO17   | LED Anode (+) |
| LED Cathode (-) | Resistor → GND |

> ⚠️ Always use a resistor to prevent LED damage.

---

## 🧠 Software Requirements

- Python 3
- RPi.GPIO library


```bash
pip install RPi.GPIO
