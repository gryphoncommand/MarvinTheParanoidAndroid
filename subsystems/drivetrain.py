from wpilib.command.subsystem import Subsystem
from wpilib.drive import MecanumDrive
from ctre import WPI_TalonSRX

from robotmap import axes
from commands.followjoystick import FollowJoystick


class Drivetrain(Subsystem):
    """
    Subsystem that holds everything for the robot's drivetrain.

    Provides methods for driving the robot on a Cartesian plane.
    """

    def __init__(self):

        # Hardware
        self.motor_lf = WPI_TalonSRX(1)
        self.motor_lr = WPI_TalonSRX(2)
        self.motor_rf = WPI_TalonSRX(3)
        self.motor_rr = WPI_TalonSRX(4)
        self.drive = MecanumDrive(
            self.motor_lf, self.motor_lr, self.motor_rf, self.motor_rr
        )

        self.drive.setExpiration(0.1)

        self.drive.setSafetyEnabled(True)

    def inputNoise(self, input):
        """
        This function limits the joystick input noise by increasing the
        tolerance for the zero value.
        """
        return input if abs(input) < 0.03 else 0

    def driveCartesian(self, xSpeed, ySpeed, zRotation, gyroAngle=0.0):
        """
        Wrapper method that the subsystem uses to input a truncated number into
        the drivetrain, along with any motor inversions.
        """
        xSpeed = self.inputNoise(xSpeed) * axes.motor_inversion[0]
        ySpeed = self.inputNoise(ySpeed) * axes.motor_inversion[1]
        zRotation = zRotation * axes.motor_inversion[2]

        self.drive.driveCartesian(xSpeed, ySpeed, zRotation, gyroAngle)

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())

    def set(self, ySpeed, xSpeed, zRotation, gyroAngle):
        """
        Shorthand method for driveCartesian.
        """
        self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)
