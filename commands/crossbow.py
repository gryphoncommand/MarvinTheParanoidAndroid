from wpilib.command import Command

import time

import subsystems

length = 5


class Crossbow(Command):
    """
    Command that controls the 'crossbow', the mechanism that grabs
    hatches on the back of the robot.

    It takes in two parameters:
        - 'speed': The speed from -1 to 1 the motor runs at.
        - 'time': The duration of the command in seconds.
    """

    def __init__(self, speed, _len):
        super().__init__("Crossbow")

        # Quantities
        self.stime = None
        self.speed = speed
        self.tlen = _len

    def initialize(self):
        self.stime = time.time()

    def execute(self):
        subsystems.mechanisms.set_crossbow(self.speed)
        self.isDone = time.time() - self.stime > self.tlen

    def end(self):
        subsystems.mechanisms.set_crossbow(0)

    def isFinished(self):
        return self.stime is not None and time.time() - self.stime > self.tlen

    def interrupted(self):
        self.end()
