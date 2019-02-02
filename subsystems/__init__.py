import wpilib

from .drivetrain import Drivetrain
from .mechanisms import Mechanisms

drivetrain = None
mechanisms = None


def init():

    global drivetrain, mechanisms

    drivetrain = Drivetrain()
    mechanisms = Mechanisms()

