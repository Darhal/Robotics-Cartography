# Import from ev3dev LargeMotor and the necessary pins
from ev3dev.auto import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
# Import from the time library the sleep function
from time import sleep

# define PI constant
PI = 3.141592653589793

"""
@class: RobotMotor
@brief: RobotMotor class to handle robots wheels and movment
"""
class RobotMotor(object):
    """
        @function: constructor
        @brief: Intilize the motors using the specified pins, 
            given diam of the wheel of the robot and the width.
    """
    def __init__(self, diam, width, r_address=OUTPUT_A, l_address=OUTPUT_D):
        super(RobotMotor, self).__init__() # call super class constructor
        self.diam = diam # set the diamter wheel
        self.width = width # set width of the robot
        # collect all robots in addreses and intilize LargeMotor
        self.motors = [LargeMotor(address) for address in (r_address, l_address)]
        self.reset_position() # reset robots psotion

    """
        @function: go_forwards
        @brief: Function to move the motors forward
        @params: distance -> The distance to walk
                 dc -> duty cycle
    """
    def go_forwards(self, distance=None, dc=60):
        if distance != None: # If distance isnt none
            turns = distance/(self.diam * PI) # calculate wheel turns based on the diameter and the distance

            for m in self.motors: # for all motors
                m.duty_cycle_sp = dc # set its duty cycle
                m.position_sp = turns*360 # set new wheel position in terms of turns mulitiplied by 360 to achieve full circle
                m.run_to_rel_pos() # call the function to start rotating the wheels
            while 'running' in self.motors[0].state: sleep(0.01) # while motor state is running then sleep
        else: # if distance is undefined then
            for m in self.motors: # for all motors
                m.duty_cycle_sp = dc # set duty cycle
                m.run_direct() # run forever using the duty cycle

    """
        @function: go_backwards
        @brief: Function to move the motors backward
        @params: distance -> The distance to walk
                 dc -> duty cycle
    """
    def go_backwards(self, distance=None, dc=60):
        if distance != None: distance = -distance # if distance isnt none then inverse it
        self.go_forwards(distance, -dc) # call go_forwards with negative duty cycle

    """
        @function: turn_left
        @brief: Function to turn the robot to the left
        @params: angle -> The rotation angle
                 dc -> duty cycle
    """
    def turn_left(self, angle=None, dc=60):
        if angle != None: # if angle is not None
            turns_per_spin = self.width/self.diam # calculate the turns per spin by dividing the robot width by the wheel diameter
            turns = (angle/360.0) * turns_per_spin # calculate the motor turns based on the angle and turns_per_spin

            for m in self.motors: # for every wheel motor that the robot have
                m.duty_cycle_sp = dc # set duty cycle
                m.position_sp = turns*360 # set new position in terms of turns
                m.run_to_rel_pos() # run motor till it reach that position
                dc = -dc # negate dc
                turns = -turns # negate turns
            while 'running' in self.motors[0].state: sleep(0.01) # while motors are still turning then wait
        else:
            for m in self.motors: # for all motors
                m.duty_cycle_sp = dc # set duty cycle
                m.run_direct() # run forever
                dc = -dc # negate duty cycle

    """
        @function: turn_right
        @brief: Function to turn the robot to the left
        @params: angle -> The rotation angle
                 dc -> duty cycle
    """
    def turn_right(self, angle=None, dc=60):
        if angle != None: angle = -angle # negate angle
        self.turn_left(angle, -dc) # turn_left with negative angle and negative dc is turning left

    """
        @function: stop
        @brief: stop the motors
    """
    def stop(self):
        for m in self.motors: # for every motor
            m.stop() # stop it

    """
        @function: reset_position
        @brief: reset position of motors
    """
    def reset_position(self): 
        for m in self.motors: # for every motor
            m.position = 0 # reset its position to 0
