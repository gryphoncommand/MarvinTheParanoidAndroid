import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import Spark

from wpilib.drive import MecanumDrive
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib.digitalinput import DigitalInput


class Mechanisms(Subsystem):

    def __init__(self):

        #stopper trigger (on instake)
        self.stopper = DigitalInput(0)
        self.intake_toggle = False

        # Verify motor ports when placed on frame
        self.intake = Spark(1)
        self.intake_solenoid = DoubleSolenoid(2, 3)
        self.intake_solenoid.set(wpilib.DoubleSolenoid.Value.kOff)

        self.gear_shift = DoubleSolenoid(0, 1)
        self.gear_shift.set(DoubleSolenoid.Value.kOff)

        self.crossbow = Spark(0)

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
        stopper = self.stopper.get()
        if stopper == False:
            return True
        elif stopper:
            return False

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())
