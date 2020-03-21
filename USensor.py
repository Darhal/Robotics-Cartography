from ev3dev.ev3 import * # ev3dev

"""
    @class: USensor
    @brief: class to handle ultra sound sensor
"""
class USensor:
    """
        @function: constructor
        @brief: constructs the ultrasensor
    """
    def __init__(self):
        self.us = UltrasonicSensor() # Ultra sonic sensor constructs
        self.us.mode = 'US-DIST-CM' # set measurment mode


    """
        @function: get_distance
        @brief: get_distance as cm
    """
    def get_distance(self):
        return self.us.value() / 10 # Convert mm to cm
