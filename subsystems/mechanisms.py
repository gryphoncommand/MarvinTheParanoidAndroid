import wpilib
from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX

from wpilib.drive import MecanumDrive
from wpilib.doublesolenoid import DoubleSolenoid


class Mechanisms(Subsystem):

    def __init__(self):

        # Verify motor ports when placed on frame
        self.intake = WPI_TalonSRX(6)
        self.intake_solenoid = DoubleSolenoid(2, 3)
        self.intake_solenoid.set(wpilib.DoubleSolenoid.Value.kOff)

        self.gear_shift = DoubleSolenoid(0, 1)
        self.gear_shift.set(DoubleSolenoid.Value.kOff)

        self.crossbow = WPI_TalonSRX(5)

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

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())
