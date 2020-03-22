#!/usr/bin/python3

# Import all necessary libraries :
from ev3dev.auto import INPUT_1, INPUT_2, INPUT_3, INPUT_4, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, \
    UltrasonicSensor, TouchSensor, ColorSensor
from RobotMotor import * # Import RobotMotor
from Sensor import * # Import Sensor
from Robot import * # Import Robot

"""
    - This script is only for urgent cases to stop the motor
"""
robot = Robot() #  Initlize the robot object
robot.stop() # stop everything