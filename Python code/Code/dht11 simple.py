#!/usr/bin/python
# Import the Adafruit_DHT library
import Adafruit_DHT

# Set the sensor type (DHT11), pin number, and retry count.
sensor = Adafruit_DHT.DHT11
pin = 21  # GPIO pin to which the sensor is connected(40 no pin)

# Attempt to read temperature and humidity data from the sensor.
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Check if the reading was successful.
if humidity is not None and temperature is not None:
    # Print temperature and humidity values.
    print('Temperature: {0:0.1f}°C'.format(temperature))
    print('Humidity: {0:0.1f}%'.format(humidity))
else:
    # Print an error message if the reading failed.
    print('Failed to read sensor data. Please check the connection and try again.')
