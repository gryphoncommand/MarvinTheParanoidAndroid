import wpilib

from commandbased import CommandBasedRobot
import subsystems
import oi
import argparse
from commands.shooter import Shooter
from commands.followjoystick import FollowJoystick
from commands.intake import Intake
# parser = argparse.ArgumentParser()
# parser.add_argument("--enabletank",
#                     help=
#                       "Pass this to override mecanum and enable tankdrive",
#                     action="store_true")
# args = parser.parse_args()


class Penumbra(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()

        oi.init()
        self.teleopProgram = wpilib.command.CommandGroup()
        self.teleopProgram.addParallel(FollowJoystick())
        self.teleopProgram.addParallel(Shooter())


    def teleopInit(self):
        self.teleopProgram.start()


if __name__ == "__main__":
    wpilib.run(Penumbra, physics_enabled=True)
