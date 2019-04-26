from .drivetrain import Drivetrain
from .mechanisms import Mechanisms
from networktables import NetworkTables


drivetrain = None
mechanisms = None
smartdashboard = None


def init():

    global drivetrain
    global mechanisms
    global smartdashboard

    drivetrain = Drivetrain()
    mechanisms = Mechanisms()

    NetworkTables.initialize("10.39.66.2")
    smartdashboard = NetworkTables.getTable("SmartDashboard")
