from wpilib.analogpotentiometer import AnalogPotentiometer
from wpilib.interfaces.pidsource import PIDSource
import subsystems


class PIDHatchSource(PIDSource):
    def __init__(self):
        self.thingie = 1

    def pidGet(self):
        source = subsystems.smartdashboard.getNumber("target_x", 0.5)

        print("Vision Source: ", source)
        return source

    def setPIDSourceType(self, v):
        if v != PIDSource.PIDSourceType.kDisplacement:
            raise Exception("Must use displacement for navx")

    def getPIDSourceType(self):
        return PIDSource.PIDSourceType.kDisplacement
