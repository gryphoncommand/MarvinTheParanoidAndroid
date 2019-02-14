from wpilib.command import Command

import subsystems
import oi
import wpilib
from robotmap import axes


class Intake(Command):
    '''
    This command runs the intake based on the triggers.
    '''
    def __init__(self):
        super().__init__('Intake')

    def initialize(self):
        pass

    def execute(self):
        if oi.joystick.getRawButton(7):
            power = 0.5
        elif oi.joystick.getRawButton(8):
            power = -0.5
        else: power = 0.0
        subsystems.mechanisms.set_intake(power)

    def end(self):
        subsystems.mechanisms.set_intake(0)
