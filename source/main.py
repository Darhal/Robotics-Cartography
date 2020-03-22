#!/usr/bin/python3

# Import everthing we need:
# Import bins, Ultasonicsensor, touchsensor, ColorSensor
from ev3dev.auto import INPUT_1, INPUT_2, INPUT_3, INPUT_4, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, \
    UltrasonicSensor, TouchSensor, ColorSensor
from RobotMotor import * # Import RobotMotor
from USensor import * # Import USensor
from Robot import * # Import Robot

# Create Robot Object:
robot = Robot()

# Start exploring around:
robot.start()