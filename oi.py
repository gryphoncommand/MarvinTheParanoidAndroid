from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.crossbow import Crossbow, PullIntake
from commands.invertmotors import InvertMotors
from commands.turnrdrive import TurnDrive
from commands.intake import Intake

joystick = None


def init():
    global joystick
    joystick = Joystick(0)

    crossbow = JoystickButton(joystick, 5)
    crossbow_in = JoystickButton(joystick, 6)

    solenoid_intake = JoystickButton(joystick, 1)

    invert_motors = JoystickButton(joystick, 2)
    invert_motors.whenPressed(InvertMotors())

    crossbow.whenPressed(Crossbow(0.75, 0.5))
    crossbow_in.whenPressed(Crossbow(-0.75, 0.5))
    solenoid_intake.whenPressed(PullIntake())

    align_hatch = JoystickButton(joystick, 12)
    align_hatch.whenPressed(TurnDrive())

    intake = JoystickButton(joystick, 4)
    intake.toggleWhenPressed(Intake())
