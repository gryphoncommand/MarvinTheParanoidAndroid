import wpilib
from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX

from wpilib.drive import MecanumDrive


class Drivetrain(Subsystem):

    def __init__(self):

        # Verify motor ports when placed on frame
        self.motor_lf = WPI_TalonSRX(1)
        self.motor_lr = WPI_TalonSRX(2)
        self.motor_rf = WPI_TalonSRX(3)
        self.motor_rr = WPI_TalonSRX(4)

        self.motor_lf.setInverted(False)
        self.motor_lr.setInverted(False)

        self.drive = MecanumDrive(self.motor_lf, self.motor_lr,
                                  self.motor_rf, self.motor_rr)

        self.drive.setExpiration(0.1)

        self.drive.setSafetyEnabled(True)

    def driveCartesian(self, ySpeed, xSpeed, zRotation, gyroAngle=0.0):
        self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())

    def set(self, ySpeed, xSpeed, zRotation, gyroAngle):
        self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)
