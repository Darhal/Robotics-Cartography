from ev3dev.auto import INPUT_1, INPUT_2, INPUT_3, INPUT_4, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, \
    UltrasonicSensor, TouchSensor, ColorSensor
from RobotMotor import *
from Sensor import *

class Robot:
    def __init__(self):
        self.moteur = RobotMotor(5.5, 14.0, OUTPUT_A, OUTPUT_D)
        self.sensor = Sensor()
        self.ts = TouchSensor()
        self.is_running = False

    def start(self):
        while (self.ts.value()):
            if self.sensor.get_distance() < 2:
                self.moteur.stop()
            else:
                self.moteur.go_forwards()


    # def stop(self):
    # TODO