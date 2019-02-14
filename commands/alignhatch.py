
import wpilib
from wpilib.interfaces.pidsource import PIDSource
from wpilib.pidcontroller import PIDController

from networktables import NetworkTables
import subsystems
from navx import AHRS

import wpilib
from wpilib.command import Command
import oi


class HatchPidSource(PIDSource):
    def __init__(self, target_x_key, default):
        self.target_x_key = target_x_key

    def pidGet(self):
        target_x = subsystems.smartdashboard.getNumber(self.target_x_key)

        #return target_x
        return 0.2


class AlignHatch(Command):
    def __init__(self):
        super().__init__('AlignHatch')

        default = 0.5

        # PIDSource Init
        src = HatchPidSource("center_x", default)
        
        self.ahrs = AHRS.create_spi()

        self.stick = oi.joystick

        self.kP = 0.75
        self.kI = 0.00
        self.kD = 0.00
        self.kF = 0.00

        def output(pid_write):
            currentRotationRate = self.stick.getTwist()
            rotationRate = pid_write + currentRotationRate
            print("Pid Write: ", pid_write)
            print('OUTPUT CALLED')
            # need to make ahrs a subsystem
            subsystems.drivetrain.driveCartesian(oi.joystick.getX(),
                                                 oi.joystick.getY(), 
                                                 rotationRate,
                                                 self.ahrs.getAngle())

        self.PID = PIDController(
            self.kP, self.kI, self.kD, self.kF, 
            src,
            output
        )

        self.PID.setInputRange(0, 1)
        self.PID.setOutputRange(-1, 1)
        self.PID.setContinuous(False)

        self.PID.setAbsoluteTolerance(0.05)

        self.PID.setPIDSourceType(PIDController.PIDSourceType.kDisplacement)

    def initialize(self):
        self.PID.enable()
        self.PID.setSetpoint(0.5)

    def execute(self):
        wpilib.SmartDashboard.putData("Hatch PID", self.PID)

    def end(self):
        self.PID.disable()

    def isFinished(self):
        target_x = subsystems.smartdashboard.getNumber("target_x", 0)
        return target_x >= .45 and target_x <= .55

    def interrupted(self):
        self.end()

