from wpilib.command import Command
import subsystems
import oi
import wpilib
import time

# from hardware.navx import NavX
# from robotmap import navx_type
from navx import AHRS
from robotmap import config


def inputNoise(input):
    if abs(input) < 0.03:
        input = 0
    return input


class AutoJoystick(Command):
    """
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    """

    def __init__(self):
        super().__init__("Follow Joystick")
        self.stime = None

        # Communicate w/navX MXP via the MXP SPI Bus.
        # - Alternatively, use the i2c bus.
        # See http://navx-mxp.kauailabs.com/guidance/selecting-an-interface/
        # for details
        #

        self.kP = 0.75
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

        # Add the PID Controller to the Test-mode dashboard, allowing manual
        # tuning of the Turn Controller's P, I and D coefficients.
        # Typically, only the P value needs to be modified.
        wpilib.Sendable.setName(turnController, "RotateController")
        self.tm = wpilib.Timer()
        self.tm.start()
        self.stick = oi.joystick
        self.xInv = -1
        self.yInv = -1
        self.zInv = 1

        if config.centric:
            self.angle = self.ahrs.getAngle()
        else:
            self.angle = 0
        self.toggle = False

    def initalize(self):
        self.stime = time.time()

    def dumpInfo(self, x_speed, y_speed, z_speed, angle):
        subsystems.smartdashboard.putNumber("x_speed", x_speed)
        subsystems.smartdashboard.putNumber("y_speed", y_speed)
        subsystems.smartdashboard.putNumber("z_speed", z_speed)
        subsystems.smartdashboard.putNumber("angle", angle)

    def execute(self):
        # print("NavX Gyro", self.ahrs.getYaw(), self.ahrs.getAngle())
        self.toggle = subsystems.mechanisms.get_stopper()

        rotateToAngle = False
        angle = self.stick.getPOV(0)
        xSpeed = 0
        ySpeed = 0
        if angle == 90:
            xSpeed = 0.3
        elif angle == 270:
            xSpeed = -0.3

        if angle == 180:
            ySpeed = 0.3
        elif angle == 0:
            ySpeed = -0.3

        if self.stick.getRawButton(2):
            self.ahrs.reset()

        if rotateToAngle:
            self.turnController.enable()
            currentRotationRate = self.rotateToAngleRate
        else:
            self.turnController.disable()
            currentRotationRate = self.stick.getTwist()

        subsystems.drivetrain.driveCartesian(
            inputNoise(oi.joystick.getX() + xSpeed) * self.xInv,
            inputNoise(oi.joystick.getY() + ySpeed) * self.yInv,
            (currentRotationRate * self.zInv) / 2,
            self.angle,
        )

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
