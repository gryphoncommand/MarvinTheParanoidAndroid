import wpilib

from commandbased import CommandBasedRobot
import subsystems
import oi
import argparse
from commands.shooter import Shooter
from commands.followjoystick import FollowJoystick
from commands.intake import Intake
from commands.crossbow import Crossbow

class Marvin(CommandBasedRobot):

    """
    This class runs a Command Based architecture, which separates the project
    into subsystems and commands. Subsystems are interfaces to provide the
    functionality, whereas commands use the functionality.

    For more information on Command Based Programming, see `this link`_.

    In addition to the methods down below, there are also methods such as
    :func:`teleopPeriodic()` and :func:`autonomousPeriodic`.
    """

    def robotInit(self):
        """
        We use this method to declare the various, high-level objects for the
        robot.
        
        For example, we can use the create a CommandGroup object to store the
        various process for our robot to run when we enable it.
        """
        subsystems.init()

        oi.init()
        self.teleopProgram = wpilib.command.CommandGroup()
        self.teleopProgram.addParallel(FollowJoystick())
        self.teleopProgram.addParallel(Shooter())

        self.autoProgram = wpilib.command.CommandGroup()
        self.autoProgram.addParallel(FollowJoystick())
        self.autoProgram.addParallel(Shooter())
        self.autoProgram.addSequential(Crossbow(.55,0.5))
        self.autoProgram.addSequential(Crossbow(-.75,1))

    def teleopInit(self):
        self.teleopProgram.start()

    def autonomousInit(self):
        self.autoProgram.start()
 


if __name__ == "__main__":
    wpilib.run(Marvin, physics_enabled=True)
