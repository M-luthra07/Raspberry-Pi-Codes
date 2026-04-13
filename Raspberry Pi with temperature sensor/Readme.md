# 🌡️ Raspberry Pi Temperature Monitoring (DHT11)

A simple IoT project using Raspberry Pi and DHT11 sensor to measure temperature and humidity using Python.

---

## 📸 Project Preview

### 🔌 Hardware Setup
![Setup](Raspberry Pi with temperature sensor/CircuitSetup .jpeg )

### 💻 Output 
![Output](Raspberry Pi with temperature sensor/Output.jpeg)

---

## 🧰 Components

- Raspberry Pi
- DHT11 Sensor
- Jumper Wires

---

## 🔌 Connections

| DHT11 | Raspberry Pi |
|------|-------------|
| VCC  | 3.3V (Pin 1) |
| DATA | GPIO4 (Pin 7) |
| GND  | Ground (Pin 6) |

---

## ⚙️ Setup Instructions

```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

---

## ▶️ Run

```bash
python3 DHT.py
```

---

❗ Troubleshooting

### Error:
```
AttributeError: 'str' object has no attribute 'formal'
```

### Fix:
Use `.format()` or `f-strings` instead of `formal`

---

## 🚀 Future Scope

- Flask Web Dashboard
- MySQL Database Storage
- Live Graph Visualization
- IoT Cloud Integration

---

## 👨‍💻 Author

Manya Luthra

---

⭐ Star this repo if you like it!
