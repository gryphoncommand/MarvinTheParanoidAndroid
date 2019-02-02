from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.crossbow import Crossbow, PullIntake
from commands.followjoystick import InvertMotors
joystick = None


def init():
    global joystick
    joystick = Joystick(0)
    crossbow = JoystickButton(joystick, 5)
    crossbow_in = JoystickButton(joystick, 6)
    solenoid_intake = JoystickButton(joystick, 1)

    invert_motors = JoystickButton(joystick, 4)
    invert_motors.whenPressed(InvertMotors())

    crossbow.whenPressed(Crossbow(0.5, 0.5))
    crossbow_in.whenPressed(Crossbow(-0.5, 0.5))
    solenoid_intake.whenPressed(PullIntake())
