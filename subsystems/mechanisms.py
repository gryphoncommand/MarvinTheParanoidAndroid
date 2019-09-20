import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import Spark
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib.digitalinput import DigitalInput

from commands.followjoystick import FollowJoystick


class Mechanisms(Subsystem):
    """
    Subsystem with miscellaneous parts of the robot.

    Includes many 'getters' and 'setters' for those different parts.
    """
    def __init__(self):

        # Hardware
        self.stopper = DigitalInput(0)
        self.crossbow = Spark(0)
        self.intake = Spark(1)
        self.gear_shift = DoubleSolenoid(0, 1)
        self.intake_solenoid = DoubleSolenoid(2, 3)

        # Quantities
        self.intake_toggle = False

        self.intake_solenoid.set(wpilib.DoubleSolenoid.Value.kOff)
        self.gear_shift.set(DoubleSolenoid.Value.kOff)

    def set_crossbow(self, speed):
        self.crossbow.set(speed)

    def get_crossbow(self):
        return self.crossbow.get()

    def set_intake(self, speed):
        self.intake.set(speed)

    def pull_intake(self, setting):
        self.intake_solenoid.set(setting)

    def shift_gears(self, _setting):
        self.gear_shift.set(_setting)

    def get_stopper(self):
        stopperState = self.stopper.get()
        if not stopperState:
            return True
        elif stopperState:
            return False

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())
