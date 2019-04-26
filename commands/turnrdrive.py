from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from pid.pidhatch import PIDHatchSource
import oi

# from navx import AHRS


class TurnDrive(Command):
    def __init__(self):
        super().__init__("TurnDrive")

        self.stick = oi.joystick

        # self.ahrs = AHRS.create_spi()

        def set_motors(pw):
            """
            currentRotationRate = self.stick.getTwist()
            rotationRate = pw + currentRotationRate
            print("Pid Write: ", pw)

            subsystems.drivetrain.driveCartesian(oi.joystick.getX(),
                                                 oi.joystick.getY(),
                                                 rotationRate,
                                                 0)
            """
            currentRate = oi.joystick.getX()
            changeRate = pw + currentRate
            print("Pid Write: ", pw)
            subsystems.drivetrain.driveCartesian(
                oi.joystick.getX(), oi.joystick.getY(), changeRate, 0
            )

        src = PIDHatchSource()

        self.kP = 0.9
        self.kI = 0.05
        self.kD = 0.00
        self.kF = 0.00

        self.PID = PIDController(
            self.kP, self.kI, self.kD, self.kF, src, set_motors
        )

        self.PID.setInputRange(0.0, 1.0)
        self.PID.setOutputRange(-0.7, 0.7)
        self.PID.setContinuous(True)
        self.PID.setAbsoluteTolerance(0.005)

        self.PID.setPIDSourceType(PIDController.PIDSourceType.kDisplacement)

        self.PID.disable()

    def initialize(self):
        self.PID.setSetpoint(0.5)
        self.PID.enable()

    def execute(self):
        pass

    def end(self):
        self.PID.disable()

    def isFinished(self):
        return self.PID.onTarget()

    def interrupted(self):
        self.end()
