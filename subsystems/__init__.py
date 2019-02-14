import wpilib

from .drivetrain import Drivetrain
from .mechanisms import Mechanisms
from networktables import NetworkTables


drivetrain = None
mechanisms = None
smartdashboard = None


def init():

    global drivetrain; global mechanisms; global smartdashboard

    drivetrain = Drivetrain()
    mechanisms = Mechanisms()

    smartdashboard = NetworkTables.getTable('SmartDashboard')

