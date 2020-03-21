from ev3dev.ev3 import *
from time import sleep

class SensorMotor:
    def __init__(self, adress = OUTPUT_C):
        self.motor = Motor(adress)
        self.reset_position()

    def turn_left(self, angle=None, dc=45):
        """docstring for turn_right"""
        m = self.motor

        if angle != None:
            turns_per_spin = 1# self.width/self.diam
            turns = (angle/360.0) * turns_per_spin

            m.duty_cycle_sp = dc
            m.position_sp = turns*360.0
            m.run_to_rel_pos()
            dc = -dc
            turns = -turns
            while 'running' in m.state: sleep(0.01)
        else:
            m.duty_cycle_sp = dc
            m.run_direct()
            dc =180-dc

    def turn_right(self, angle=None, dc=45):
        if angle != None: angle = -angle
        self.turn_left(angle, -dc)

    def stop(self):
        self.motor.stop()

    def reset_position(self):
        self.motor.position = 0

