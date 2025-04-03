# Created by: Michael Bruneau
# Created on: April 2025
#
# This module is a Raspberry Pi Pico program that displays distance from sonar and turns the Micro sevro if an object gets within 50cm close to the sonar


import time
import board
import adafruit_hcsr04
import digitalio
import pwmio
from adafruit_motor import servo


# variables
seconds_to_microseconds_conversion_number = 1000000
sonar_delays = [2 / seconds_to_microseconds_conversion_number, 10 / seconds_to_microseconds_conversion_number]
delay_between_sonar_cheeks = 10
distance = 0
servo_delay = 0.5
TOO_CLOSE = 50

# setup
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.GP15, echo_pin = board.GP14)

# create a PWMOut object on Pin GP12.
pwm = pwmio.PWMOut(board.GP12 , duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

# loop
while True:
    # Sonar gets the distance form object
    time.sleep(sonar_delays[0])
    distance = sonar.distance
    time.sleep(sonar_delays[1])

    #print(f"Distance: {distance} cm")

    # Turns on LED if an object’s distance is equal to or closer then 20 cm from the sonar
    if distance < TOO_CLOSE:
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(servo_delay)
    else:
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(servo_delay)

    # The commented out code is not part of the actual code but is needed to get it working by uncommenting it and then recommenting it
    #time.sleep(delay_between_sonar_cheeks)
