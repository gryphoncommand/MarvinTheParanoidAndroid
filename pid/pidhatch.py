from wpilib.analogpotentiometer import AnalogPotentiometer
from wpilib.interfaces.pidsource import PIDSource


class PIDHatchSource(PIDSource):
    def __init__(self, _source):
        self.source = _source

    def pidGet(self):
        source = self.source
        print("Vision Source: ", source)
        return source

    def setPIDSourceType(self, v):
        if v != PIDSource.PIDSourceType.kDisplacement:
            raise Exception("Must use displacement for navx")

    def getPIDSourceType(self):
        return PIDSource.PIDSourceType.kDisplacement

    