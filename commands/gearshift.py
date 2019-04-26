from wpilib.command import Command
import subsystems
import wpilib


class GearShift(Command):
    def __init__(self):
        super().__init__("GearShift")
        self.default = False
        subsystems.mechanisms.shift_gears(wpilib.DoubleSolenoid.Value.kOff)

    def execute(self):
        print("In Gearshift::execute()")
        if self.default:
            subsystems.mechanisms.shift_gears(
                wpilib.DoubleSolenoid.Value.kForward
            )
        else:
            subsystems.mechanisms.shift_gears(
                wpilib.DoubleSolenoid.Value.kReverse
            )
        self.default = not self.default
        self.isDone = True

    def isFinished(self):
        return self.isDone
