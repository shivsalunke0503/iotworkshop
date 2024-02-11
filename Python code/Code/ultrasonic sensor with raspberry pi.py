import RPi.GPIO as GPIO  # Import the RPi.GPIO library
import time             # Import the time module

# Define GPIO pins for the ultrasonic sensor
TRIG = 23
ECHO = 24

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Enter an infinite loop for continuous distance measurement
while True:
    print("Distance measurement in progress...")

    # Set up the TRIG and ECHO pins
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    # Ensure a clean signal on the TRIG pin
    GPIO.output(TRIG, False)

    # Wait for the sensor to settle
    time.sleep(0.2)

    # Generate a short trigger pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure the duration of the echo pulse
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate the pulse duration and convert it to distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound (cm/s)
    distance = round(distance, 2)      # Round to 2 decimal places

    # Print the distance measured
    print('Distance: {0} cm'.format(distance))

    # Wait for 2 seconds before the next measurement
    time.sleep(2)
