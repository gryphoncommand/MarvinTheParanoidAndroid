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
        self.toggle = False

    def initialize(self):
        pass

    def execute(self):
        self.toggle = subsystems.mechanisms.get_stopper()
        print(self.toggle)

        subsystems.mechanisms.set_intake(0.5)

    def isFinished(self):
        return self.toggle

    def end(self):
        subsystems.mechanisms.set_intake (0)
