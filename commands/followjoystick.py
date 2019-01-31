from wpilib.command import Command
import subsystems
import oi
import math
import wpilib


def inputNoise(input):
    if(abs(input) < 0.03):
        input = 0
    return input


class FollowJoystick(Command):
    '''
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    '''
    def __init__(self):
        super().__init__('Follow Joystick')
        # self.requires(subsystems.drivetrain)

    def execute(self):
        subsystems.drivetrain.driveCartesian(
                        inputNoise(oi.joystick.getX()),
                        inputNoise(oi.joystick.getY()),
                        inputNoise(oi.joystick.getZ()), 0)


class GearShift(Command):
    def __init__(self):
        super().__init__('GearShift')
        self.default = False
        subsystems.mechanisms.shift_gears(wpilib.DoubleSolenoid.Value.kOff)

    def execute(self):
        print('In Gearshift::execute()')
        if self.default:
            subsystems.mechanisms.shift_gears(wpilib.DoubleSolenoid.Value.kForward)
        else:
            subsystems.mechanisms.shift_gears(wpilib.DoubleSolenoid.Value.kReverse)
        self.default = not self.default
        self.isDone = True
    
    def isFinished(self):
        return self.isDone
