from RobotMotor import *
from Sensor import *
from Robot import *
from Image import *

class Explore:
    def __init__(self):
        self.robot = Robot()
        self.img = Image("explore.png", 1028, 1028)
    
    def start(self):
        self.robot.start(self.img)