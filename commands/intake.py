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
        self.control = True

    def initialize(self):
        pass

    def execute(self):
        if self.control:
            subsystems.mechanisms.set_intake(.5)


    def end(self):
        subsystems.mechanisms.set_intake(0)
