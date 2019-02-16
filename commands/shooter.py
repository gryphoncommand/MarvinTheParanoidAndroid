from wpilib.command import Command
import subsystems
import oi
import wpilib


class Shooter(Command):
    '''
    SHoots the ball out the top
    '''
    def __init__(self):
        super().__init__('Shooter')
        self.stick = oi.joystick

    def initialize(self):
        pass

    def execute(self):
        if self.stick.getRawButton(6):
            power = 1
        elif self.stick.getRawButton(8):
            power = -1.0
        else: 
            power = 0.0
        subsystems.mechanisms.set_intake(power)

    def end(self):
        subsystems.mechanisms.set_intake(0)
