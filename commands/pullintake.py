import wpilib
from wpilib.command import Command
import time

import subsystems


class PullIntake(Command):
    """
    Command that runs the piston that pushes/pulls the arm up and down.

    It operates on a toggle basis, meaning that when you run the command,
    the value of the piston is flipped.
    """
    def __init__(self):
        super().__init__("PullIntake")
        self.default = False
        subsystems.mechanisms.pull_intake(wpilib.DoubleSolenoid.Value.kOff)

    def execute(self):
        if self.default:
            subsystems.mechanisms.pull_intake(
                wpilib.DoubleSolenoid.Value.kForward
            )
        else:
            subsystems.mechanisms.pull_intake(
                wpilib.DoubleSolenoid.Value.kReverse
            )
        self.default = not self.default
        self.isDone = True

    def isFinished(self):
        return self.isDone
