from ev3dev.ev3 import * # Import everything ev3dev.ev3 
from time import sleep # Import from time, sleep

"""
    @class: SensorMotor
    @brief: class to handle the sensor motor, 
        that is the motor used to rotate the sensor 180 degrees in the front 
"""
class SensorMotor:
    """
        @function: constructor
        @brief: initlize sensor motor
    """
    def __init__(self, adress = OUTPUT_C):
        self.motor = Motor(adress) # Intilize the MeduimMotor at the given adress
        self.reset_position() # reset position to 0


    """
        @function: turn_left
        @brief: function to turn the motor to the left
    """
    def turn_left(self, angle=None, dc=45):
        m = self.motor # intilise motor array to m
        if angle != None: # if the angle != None
            turns = (angle/360.0) * 1 # calculate turns based of the angle

            m.duty_cycle_sp = dc # set the duty cycle
            m.position_sp = turns*360.0 # set position in terms of turns
            m.run_to_rel_pos() # run till reach position
            dc = -dc # negate duty cycle
            turns = -turns # negate the turns
            while 'running' in m.state: sleep(0.01) # while still running wait
        else:
            m.duty_cycle_sp = dc # set duty cycle
            m.run_direct() # run forever
            dc = 180-dc # negate dc with 180 degree


    """
        @function: turn_right
        @brief: turn motor right
    """
    def turn_right(self, angle=None, dc=45):
        if angle != None: angle = -angle # negate the angle
        self.turn_left(angle, -dc) # call turn_left with negative angle and negative dc


    """
        @function: stop
        @brief: stop the motor
    """
    def stop(self):
        self.motor.stop() # stop motor


    """
        @function: reset_position
        @brief: set position
    """
    def reset_position(self):
        self.motor.position = 0 # set position to 0

