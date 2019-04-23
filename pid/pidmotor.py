from wpilib.interfaces.pidsource import PIDSource
from wpilib.interfaces.pidoutput import PIDOutput
from hardware.encoder import Encoder


class PIDMotorSource(PIDSource):
    def __init__(self, _encoder):

        self.sourceType = Encoder.PIDSourceType.kRate
        self.encoder = _encoder
        self.encoder.setSamplesToAverage(16)
        self.scale = 1.0
        self.encoder.setPIDSourceType(Encoder.PIDSourceType.kRate)

    def pidGet(self):
        return self.encoder.getRate()

    def getPIDSourceType(self):
        return self.sourceType
