from ev3dev.auto import INPUT_1, INPUT_2, INPUT_3, INPUT_4, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, \
    UltrasonicSensor, TouchSensor, ColorSensor
from RobotMotor import *
from Sensor import *
from SensorMotor import *
# from Image import *

class Robot:
    def __init__(self):
        self.moteur = RobotMotor(5.5, 14.0, OUTPUT_A, OUTPUT_D)
        self.sensor = Sensor()
        self.ts = TouchSensor()
        self.is_running = False
        self.cool_down_time = 1.0
        self.pos = (0, 0)
        # self.img = Image("explore.png", 1028, 1028)
        self.sensor_motor = SensorMotor()

    def start(self):
        self.moteur.go_forwards()
        print("* Going forward")
        dist = self.sensor.get_distance()
        senseor_left = True

        while self.ts.value():
            self.loop(dist, senseor_left)
            senseor_left = not senseor_left
            dist = self.sensor.get_distance()

        self.shutdown()

    def loop(self, dist, sens_left):
        self.pos[0] += 1
        # self.img.point(self.pos, (0, 255, 0))

        if (sens_left):
            self.sensor_motor.stop()
            self.sensor_motor.turn_left()
            print("* Turning sensor to the left")
        else:
            self.sensor_motor.stop()
            self.sensor_motor.turn_right()
            print("* Turning sensor to the right")

        if (dist > 20.0):
            self.handleObstacle()
        
        print("* My Position is : (%.2f, %.2f)" % (self.pos[0], self.pos[1]))
        sleep(self.cool_down_time)
        
    def handleObstacle(self):
        print("* Handling obstacle")

    def stop(self):
        self.moteur.stop()
        self.sensor_motor.stop()
    
    def shutdown(self):
        print("* Shutting down")
        self.stop()
        self.img.save()
    