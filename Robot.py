from ev3dev.auto import INPUT_1, INPUT_2, INPUT_3, INPUT_4, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, \
    UltrasonicSensor, TouchSensor, ColorSensor
from RobotMotor import *
from USensor import *
from SensorMotor import *
# from Image import *
from enum import Enum

class Dir(Enum):
    LEFT = 0
    FRONT = 1
    RIGHT = 2

class Robot:
    def __init__(self):
        self.moteur = RobotMotor(5.5, 14.0, OUTPUT_A, OUTPUT_D)
        self.sensor = USensor()
        self.ts = TouchSensor()
        self.is_running = False
        self.cool_down_time = 1.0
        self.posx = 0
        self.posy = 0
        # self.img = Image("explore.png", 1028, 1028)
        self.sensor_motor = SensorMotor()
        self.sensor_dir = 1
        self.obstacles = []

    def start(self):
        #self.moteur.go_forwards()
        print("* Going forward")
        dist = self.sensor.get_distance()
        print("TouchSensor: "+str(self.ts.value()))

        while not self.ts.value():
            self.loop(dist)
            self.sensor_dir =  (self.sensor_dir + 1) % 3
            dist = self.sensor.get_distance()

        self.shutdown()

    def loop(self, dist):
        self.posy += 1
        # self.img.point((self.posx, self.posy), (0, 255, 0))

        print("Distance of USensor: %0.2f"%dist)
        if (dist < 30.0):
            self.handleObstacle()

        if (self.sensor_dir == 0):
            self.sensor_motor.stop()
            sleep(0.1)
            self.sensor_motor.turn_right(None, 20)
            print("* Turning sensor to the middle")
        elif (self.sensor_dir == 1):
            self.sensor_motor.stop()
            sleep(0.1)
            self.sensor_motor.turn_right(None, 20)
            print("* Turning sensor to the right")
        elif (self.sensor_dir == 2):
            self.sensor_motor.stop()
            sleep(0.1)
            self.sensor_motor.turn_left(None)
            print("* Turning sensor to the left")
        
        print("* My Position is : (%.2f, %.2f)" % (self.posx, self.posy))
        sleep(self.cool_down_time)
        
    def handleObstacle(self):
        if (self.sensor_dir == 0):
            print("* Handling obstacle to the left")
            self.obstacles.append((self.posx, self.posy - 1))
        elif (self.sensor_dir == 1):
            print("* Handling obstacle to the middle")
            self.obstacles.append((self.posx + 1, self.posy))
        elif (self.sensor_dir == 2):
            print("* Handling obstacle to the right")
            self.obstacles.append((self.posx, self.posy - 1))

    def stop(self):
        self.moteur.stop()
        self.sensor_motor.stop()
    
    def shutdown(self):
        print("* Shutting down")
        self.stop()
        # self.img.save()
    