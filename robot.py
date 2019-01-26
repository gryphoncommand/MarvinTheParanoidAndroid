import wpilib

from commandbased import CommandBasedRobot
import subsystems
import oi

from commands.followjoystick import FollowJoystick


class Penumbra(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()

        oi.init()

        self.teleopProgram = wpilib.command.CommandGroup()
        self.teleopProgram.addParallel(FollowJoystick())

    def teleopInit(self):
        self.teleopProgram.start()


if __name__ == "__main__":
    wpilib.run(Penumbra, physics_enabled=False)
