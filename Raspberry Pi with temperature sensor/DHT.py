import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if temperature is not None:
    print("Temp = {}°C".format(temperature))
    print("Humidity = {}%".format(humidity))
else:
    print("Failed to retrieve data")
