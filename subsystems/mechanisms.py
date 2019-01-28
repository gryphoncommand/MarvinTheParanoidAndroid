import wpilib
from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX

from wpilib.drive import MecanumDrive
from wpilib.solenoid import Solenoid


class Mechanisms(Subsystem):

    def __init__(self):

        # Verify motor ports when placed on frame
        self.intake = WPI_TalonSRX(5)
        self.intake_solenoid = Solenoid(0)

        self.crossbow = WPI_TalonSRX(6)

    def set_crossbow(self, speed):
        self.crossbow.set(speed)

    def get_crossbow(self):
        return self.crossbow.get()

    def set_intake(self, speed):
        self.intake.set(speed)

    def pull_intake(self):
        self.intake_solenoid.set(not self.intake_solenoid.get())

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())
