from wpilib.command import Command
import subsystems
import oi
import math
import wpilib
from navx import AHRS
from robotmap import axes, config
import time


def inputNoise(input):
    if abs(input) < 0.03:
        input = 0
    return input


class FollowJoystick(Command):
    """
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    """

    def __init__(self):
        super().__init__("Follow Joystick")
        self.stime = None

        self.kP = 0.005
        self.kI = 0.00
        self.kD = 0.00
        self.kF = 0.00

        self.ahrs = AHRS.create_spi()

        self.kToleranceDegrees = 2.0

        turnController = wpilib.PIDController(
            self.kP, self.kI, self.kD, self.kF, self.ahrs, output=self
        )
        turnController.setInputRange(-180.0, 180.0)
        turnController.setOutputRange(-1.0, 1.0)
        turnController.setAbsoluteTolerance(self.kToleranceDegrees)
        turnController.setContinuous(True)

        self.turnController = turnController
        self.rotateToAngleRate = 0

        # Add the PID Controller to the Test-mode dashboard, allowing manual  */
        # tuning of the Turn Controller's P, I and D coefficients.            */
        # Typically, only the P value needs to be modified.                   */
        wpilib.Sendable.setName(turnController, "RotateController")
        self.tm = wpilib.Timer()
        self.tm.start()
        self.stick = oi.joystick
        self.xInv = -1
        self.yInv = -1
        self.zInv = 1

        if config.centric == True:
            self.angle = self.ahrs.getAngle()
        else:
            self.angle = 0

    def initalize(self):
        self.stime = time.time()

    def dumpInfo(self, x_speed, y_speed, z_speed, angle):
        subsystems.smartdashboard.putNumber("x_speed", x_speed)
        subsystems.smartdashboard.putNumber("y_speed", y_speed)
        subsystems.smartdashboard.putNumber("z_speed", z_speed)
        subsystems.smartdashboard.putNumber("angle", angle)

    def execute(self):
        print("NavX Gyro Yaw, Angle", self.ahrs.getYaw(), self.ahrs.getAngle())
        rotateToAngle = False

        if self.stick.getRawButton(3):
            self.turnController.setSetpoint(90.0)
            rotateToAngle = True
        if self.stick.getRawButton(2):
            self.ahrs.reset()

        if rotateToAngle:
            self.turnController.enable()
            currentRotationRate = self.rotateToAngleRate
        else:
            self.turnController.disable()
            currentRotationRate = self.stick.getTwist()

        subsystems.drivetrain.driveCartesian(
            inputNoise(oi.joystick.getX()) * self.xInv,
            inputNoise(oi.joystick.getY()) * self.yInv,
            currentRotationRate * self.zInv,
            self.angle,
        )

        # wpilib.SmartDashboard.putData("Centric Angle", self.angle)

    def pidWrite(self, output):
        """This function is invoked periodically by the PID Controller,
        based upon navX MXP yaw angle input and PID Coefficients.
        """
        self.rotateToAngleRate = output

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        return self.stime is not None and time.time() - self.stime > self.len

    def interrupted(self):
        self.end()
