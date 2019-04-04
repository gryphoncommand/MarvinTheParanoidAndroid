from wpilib.command.subsystem import Subsystem
from wpilib import PIDController
from wpilib.pidcontroller import PIDController

from ctre import WPI_TalonSRX
from robotmap import axes

from wpilib.encoder import Encoder



from robotmap import motors, encoders


class MecDrive(Subsystem):
    def __init__(self):
        super().__init__("MecanumDrive")
        self.motor_lf = WPI_TalonSRX(motors.lf)
        self.motor_lr = WPI_TalonSRX(motors.lr)
        self.motor_rf = WPI_TalonSRX(motors.rf)
        self.motor_rr = WPI_TalonSRX(motors.rr)

    def set_lf(self, power):
        self.motor_lf.set(power)

    def set_lr(self, power):
        self.motor_lr.set(power)

    def set_rf(self, power):
        self.motor_rf.set(power)
    
    def set_rr(self, power):
        self.motor_rr.set(power)
    
    def stop(self):
        self.set(0, 0, 0, 0)

    def set(self, lf_power=0, lr_power=0, rf_power=0, rr_power=0):
        if lf_power is not None:
            self.set_lf(lf_power)
        if lr_power is not None:
            self.set_lf(lr_power)
        if rf_power is not None:
            self.set_lf(rf_power)
        if rr_power is not None:
            self.set_lf(rr_power)

    