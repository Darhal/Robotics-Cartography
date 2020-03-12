from ev3dev.ev3 import *

class USensor:
    def __init__(self):
        self.us = UltrasonicSensor() # Ultra sonic sensor
        self.us.mode = 'US-DIST-CM'
    
    def get_distance(self):
        return self.us.value() / 10 # Convert mm to cm
