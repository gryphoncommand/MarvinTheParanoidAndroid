import wpilib
from wpilib.command import Command
from robotmap import axes

class InvertMotors(Command):
    def __init__(self):
        self.default = False
        super().__init__('InvertMotors')

    def execute(self):
        for item in axes.motor_inversion:
            item = item * -1