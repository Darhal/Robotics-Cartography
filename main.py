#!/usr/bin/python3

from ev3dev.auto import INPUT_1, INPUT_2, INPUT_3, INPUT_4, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, \
    UltrasonicSensor, TouchSensor, ColorSensor
from RobotMotor import *
from Sensor import *
from Robot import *

"""robot = RobotMotor(5.5, 14.0, OUTPUT_A, OUTPUT_D)
robot.go_forwards(5)"""
"""sensor = Sensor()

ts = TouchSensor()
while ts.value():
    if sensor.get_distance() < 5:
        Leds.set_color(Leds.LEFT, Leds.RED)
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)"""

robot = Robot()
robot.start()