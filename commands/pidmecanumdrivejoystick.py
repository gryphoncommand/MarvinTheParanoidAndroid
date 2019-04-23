import time

from wpilib.command import Command
from wpilib.pidcontroller import PIDController

import subsystems
import oi
from pid.pidmotor import PIDMotorSource
import oi
import math

import robotmap
import wpilib
from subsystems.mecdrive import MecDrive
from subsystems.sensors import Sensors


class PIDMecanumDriveJoystick(Command):
    """

    Joystick control the mecanum drive

    """

    def __init__(self):
        super().__init__("PIDMecanumDriveJoystick")

        drive = MecDrive()
        sensors = Sensors()

        self.stick = oi.joystick

        src = PIDMotorSource(sensors.get_lf_rate())

        self.kP = 0.9
        self.kI = 0.05
        self.kD = 0.00
        self.kF = 0.00

        self.pid = {}

        # need to implement for when motors break etc...
        self.slowest = 1

        # self.pid["lf"] = PIDController(pid.L[0], pid.L[1], pid.L[2], pid.L[3], src, drive.set_lf)
        self.pid["lr"] = PIDController(
            pid.R[0], pid.R[1], pid.R[2], pid.R[3], src, drive.set_lr
        )
        self.pid["rf"] = PIDController(
            pid.R[0], pid.R[1], pid.R[2], pid.R[3], src, drive.set_rf
        )
        self.pid["rr"] = PIDController(
            pid.R[0], pid.R[1], pid.R[2], pid.R[3], src, drive.set_rr
        )

        self.applyPID(lambda p: p.setPIDSourceType(PIDController.PIDSourceType.kRate))
        self.applyPID(lambda p: p.setOutputRange(-1, 1))
        self.applyPID(lambda p: p.setContinuous(False))
        self.applyPID(lambda p: p.setAbsoluteTolerance(0.025))

        self.xInv = -1
        self.yInv = -1
        self.zInv = 1

        # Joystick controll ranges to activate PID
        self.max_range = (-0.15, 0.15)
        self.min_range = (-0.85, 0.85)

    def initialize(self):
        self.applyPID(lambda pid: pid.enable())

    def end(self):
        self.applyPID(lambda pid: pid.disable())

    def applyPID(self, func):
        func(self.pid["lf"])
        func(self.pid["lr"])
        func(self.pid["rf"])
        func(self.pid["rr"])

    def execute(self):
        wpilib.SmartDashboard.putData("lf_speed", self.pid["lf"])
        wpilib.SmartDashboard.putData("lr_speed", self.pid["lr"])
        wpilib.SmartDashboard.putData("rf_speed", self.pid["rf"])
        wpilib.SmartDashboard.putData("rr_speed", self.pid["rr"])
        wpilib.SmartDashboard.putNumber("lf_pid_setpoint", self.pid["lf"].getSetpoint())

        subsystems.drivetrain.driveCartesian(
            oi.joystick.getX(), oi.joystick.getY(), oi.joystick.getZ(), 0
        )

    """
        if (oi.joystick.getY() not in self.min_range) and (oi.joystick.getX() in self.max_range):
            self.pid["lf"].setSetpoint(slpow)
            self.pid["lr"].setSetpoint(srpow)
            self.pid["rf"].setSetpoint(slpow)
            self.pid["rr"].setSetpoint(srpow)
    """
