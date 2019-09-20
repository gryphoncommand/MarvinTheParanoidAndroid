from wpilib.command import Command
import subsystems
import oi
import wpilib
from navx import AHRS
from robotmap import config
import time


def inputNoise(input):
    if abs(input) < 0.03:
        input = 0
    return input


class FollowJoystick(Command):
    """
    Command that reads the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.

    This operates during the Teleop period of a competition.
    """

    def __init__(self):
        super().__init__("FollowJoystick")

        # Hardware
        self.ahrs = AHRS.create_spi()
        self.stick = oi.joystick

        # Quantities
        self.angle = 0
        self.stime = None
        self.xInv = -1
        self.yInv = -1
        self.zInv = 1

        if config.centric:
            self.angle = self.ahrs.getAngle()

    def initalize(self):
        self.stime = time.time()

    def dumpInfo(self, x_speed, y_speed, z_speed, angle):
        subsystems.smartdashboard.putNumber("x_speed", x_speed)
        subsystems.smartdashboard.putNumber("y_speed", y_speed)
        subsystems.smartdashboard.putNumber("z_speed", z_speed)
        subsystems.smartdashboard.putNumber("angle", angle)

    def inputNoise(self, input):
        """
        This function limits the joystick input noise by increasing the
        tolerance for the zero value.
        """
        return input if abs(input) < 0.02 else 0

    def execute(self):
        if self.stick.getRawButton(3):
            rotateToAngle = True
        if self.stick.getRawButton(2):
            self.ahrs.reset()

        currentRotationRate = self.stick.getTwist()

        subsystems.drivetrain.driveCartesian(
            self.inputNoise(oi.joystick.getX()) * self.xInv,
            self.inputNoise(oi.joystick.getY()) * self.yInv,
            currentRotationRate * self.zInv,
            self.angle,
        )

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        return self.stime is not None and time.time() - self.stime > self.len

    def interrupted(self):
        self.end()
