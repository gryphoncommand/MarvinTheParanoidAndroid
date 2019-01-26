import wpilib

from .drivetrain import Drivetrain



drivetrain = None

def init():
    
    global drivetrain

    drivetrain = Drivetrain()