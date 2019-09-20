import wpilib
from wpilib.command import Command
from navx import AHRS
import time

import subsystems
import oi
from robotmap import config


class AutoJoystick(Command):
    """
    Command that reads the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.

    This runs in parallel with everything else during the Sandstorm.
    """

    def __init__(self):
        super().__init__("Follow Joystick")

        # Hardware
        self.ahrs = AHRS.create_spi()
        self.stick = oi.joystick

        # Quantities
        self.xInv = -1
        self.yInv = -1
        self.zInv = 1
        self.stime = None
        self.toggle = False
        self.angle = 0
        self.navxAngle = 0
        self.xSpeed = 0
        self.ySpeed = 0

        if config.centric:
            self.navxAngle = self.ahrs.getAngle()

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
        self.toggle = subsystems.mechanisms.get_stopper()

        self.angle = self.stick.getPOV(0)

        if self.angle == 90:
            self.xSpeed = 0.3
        elif self.angle == 270:
            self.xSpeed = -0.3

        if self.angle == 180:
            self.ySpeed = 0.3
        elif self.angle == 0:
            self.ySpeed = -0.3

        if self.stick.getRawButton(2):
            self.ahrs.reset()

        currentRotationRate = self.stick.getTwist()

        subsystems.drivetrain.driveCartesian(
            self.inputNoise(oi.joystick.getX() + self.xSpeed) * self.xInv,
            self.inputNoise(oi.joystick.getY() + self.ySpeed) * self.yInv,
            (currentRotationRate * self.zInv) / 2,
            self.navxAngle,
        )

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        return self.stime is not None and time.time() - self.stime > self.len

    def interrupted(self):
        self.end()
