from wpilib.command import Command

import subsystems
import wpilib

# from commands.crossbow import Crossbow, PullIntake


class Intake(Command):
    """
    This command runs the intake based on the triggers.
    """

    def __init__(self):
        super().__init__("Intake")
        self.toggle = False

    def initialize(self):
        pass

    def execute(self):
        self.toggle = subsystems.mechanisms.get_stopper()

        subsystems.mechanisms.set_intake(0.6)

    def isFinished(self):
        if self.toggle:
            wpilib.Timer.delay(0.1)
        return self.toggle

    def end(self):
        subsystems.mechanisms.set_intake(0)
