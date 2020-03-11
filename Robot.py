from ev3dev.auto import INPUT_1, INPUT_2, INPUT_3, INPUT_4, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, \
    UltrasonicSensor, TouchSensor, ColorSensor
from RobotMotor import *
from Sensor import *
from Image import *

class Robot:
    def __init__(self):
        self.moteur = RobotMotor(5.5, 14.0, OUTPUT_A, OUTPUT_D)
        self.sensor = Sensor()
        self.ts = TouchSensor()
        self.is_running = False
        self.pos = (0, 0)
        self.img = Image("explore.png", 1028, 1028)

    def start(self):
        self.moteur.go_forwards()
        dist = self.sensor.get_distance()

        while (dist > 10.0):
            self.loop(dist)
            dist = self.sensor.get_distance()

        self.shutdown()

    def loop(self, dist):
        self.pos[0] += 1
        self.img.point(self.pos, (0, 255, 0))

        if (dist > 20.0):
            self.handleObstacle()
        
    def handleObstacle(self):
        print("Obstacle")

    def stop(self):
        self.moteur.stop()
    
    def shutdown(self):
        self.stop()
        self.img.save()
    