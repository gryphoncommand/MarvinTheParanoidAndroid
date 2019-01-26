from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

joystick = None

def init():
    global joystick
    joystick = Joystick(0)


    


