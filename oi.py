from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.crossbow import Crossbow
from commands.pullintake import PullIntake
from commands.intake import Intake


joystick = None


def init():
    global joystick
    joystick = Joystick(0)

    crossbow = JoystickButton(joystick, 5)
    crossbow_in_hold = JoystickButton(joystick, 6)

    solenoid_intake = JoystickButton(joystick, 1)

    crossbow.whenPressed(Crossbow(0.8, 1))
    crossbow_in_hold.whenPressed(Crossbow(-0.6, 1.75))

    solenoid_intake.whenPressed(PullIntake())

    intake = JoystickButton(joystick, 4)
    intake.toggleWhenPressed(Intake())
