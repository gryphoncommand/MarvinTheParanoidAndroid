import time

from wpilib.command import Command

import subsystems
import oi


class DriveTimed(Command):
    def __init__(self, ySpeed, xSpeed, zRotation, gyroAngle, _len):
        super().__init__("DriveTimed")
        self.ySpeed, self.xSpeed, self.zRotation = ySpeed, xSpeed, zRotation
        self.gyroAngle, self.len = gyroAngle, _len

        self.stime = None

    def initalize(self):
        self.stime = time.time()

    def execute(self):
        subsystems.drivetrain.set(
            self.ySpeed, self.xSpeed, self.zRotation, self.gyroAngle
        )

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        return self.stime is not None and time.time() - self.stime > self.len

    def interrupted(self):
        self.end()
