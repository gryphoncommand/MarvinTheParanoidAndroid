from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.crossbow import Crossbow, PullIntake
from commands.invertmotors import InvertMotors
from commands.turnrdrive import TurnDrive
from commands.intake import Intake
#from commands.invertmotors import InvertMotors

joystick = None


def init():
    global joystick
    joystick = Joystick(0)


    crossbow = JoystickButton(joystick, 5)
    crossbow_in_hold = JoystickButton(joystick, 6)

    solenoid_intake = JoystickButton(joystick, 1)

    #invert_motors = JoystickButton(joystick, 3)
    #invert_motors.whenPressed(InvertMotors())

    crossbow.whenPressed(Crossbow(.75, 1))
    crossbow_in_hold.whenPressed(Crossbow(-0.35, 3.5))

    solenoid_intake.whenPressed(PullIntake())

    align_hatch = JoystickButton(joystick, 12)
    align_hatch.whenPressed(TurnDrive())

    intake = JoystickButton(joystick, 4)
    intake.toggleWhenPressed(Intake())
