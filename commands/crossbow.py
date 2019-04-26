from wpilib.command import Command

import subsystems
import time
import wpilib

length = 5


# class PullIntake(Command):

#     def __init__(self):
#         super().__init__('PullIntake')
#         self.isDone = False

#     def initialize(self):
#         pass

#     def execute(self):
#         subsystems.mechanisms.pull_intake()
#         self.isDone = True

#     def isFinished(self):
#         return self.isDone


class PullIntake(Command):
    def __init__(self):
        super().__init__("PullIntake")
        self.default = False
        subsystems.mechanisms.pull_intake(wpilib.DoubleSolenoid.Value.kOff)

    def execute(self):
        print("In Crossbow::execute()")
        print(self.default)
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


class Crossbow(Command):
    """
    This command sets the motor for a certain length.

    """

    def __init__(self, speed, _len):
        super().__init__("Crossbow")
        self.stime = None
        self.speed = speed
        self.tlen = _len

    def initialize(self):
        self.stime = time.time()

    def execute(self):
        # if subsystems.mechanisms.get_crossbow() > 0:
        #     subsystems.mechanisms.set_crossbow(-1 * self.speed)
        # else:
        subsystems.mechanisms.set_crossbow(self.speed)
        self.isDone = time.time() - self.stime > self.tlen

    def end(self):
        subsystems.mechanisms.set_crossbow(0)

    def isFinished(self):
        return self.stime is not None and time.time() - self.stime > self.tlen

    def interrupted(self):
        self.end()
