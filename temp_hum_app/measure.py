import RPi.GPIO as GPIO
import dht11
import datetime

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=17)

def get_temp_hum():
    result = instance.read()
    if result.is_valid():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result.temperature, result.humidity
    else:
        return None, None, None