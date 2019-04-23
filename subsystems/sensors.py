import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import Spark

from robotmap import encoders
from hardware.encoder import Encoder


class Sensors(Subsystem):
    def __init__(self):

        self.encoders = {
            "lf": Encoder(*encoders.lf),
            "lr": Encoder(*encoders.lf),
            "rf": Encoder(*encoders.lf),
            "rr": Encoder(*encoders.lf),
        }

    def get_lf_rate(self):
        return self.encoders["lf"].getRate()

    def get_lr_rate(self):
        return self.encoders["lr"].getRate()

    def get_rf_rate(self):
        return self.encoders["rf"].getRate()

    def get_rr_rate(self):
        return self.encoders["rr"].getRate()
