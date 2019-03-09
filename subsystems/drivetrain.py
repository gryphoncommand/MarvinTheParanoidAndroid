import wpilib
from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX
from commands.followjoystick import FollowJoystick
from wpilib.drive import MecanumDrive
from robotmap import axes

class Drivetrain(Subsystem):

    def __init__(self):

        # Verify motor ports when placed on frame
        self.motor_lf = WPI_TalonSRX(1)
        self.motor_lr = WPI_TalonSRX(2)
        self.motor_rf = WPI_TalonSRX(3)
        self.motor_rr = WPI_TalonSRX(4)

        self.motor_rr.setInverted(True)
        self.motor_lr.setInverted(True)

        self.drive = MecanumDrive(self.motor_lf, self.motor_lr,
                                  self.motor_rf, self.motor_rr)

        self.drive.setExpiration(0.1)

        self.drive.setSafetyEnabled(True)

    def inputNoise(self,input):
        if(abs(input) < 0.03):
            input = 0
        return input

    def driveCartesian(self, xSpeed, ySpeed, zRotation, gyroAngle=0.0):
        xSpeed = self.inputNoise(xSpeed) * axes.motor_inversion[0]
        ySpeed = self.inputNoise(ySpeed) * axes.motor_inversion[1]
        zRotation = zRotation * axes.motor_inversion[2]

        self.drive.driveCartesian(xSpeed, ySpeed, zRotation, gyroAngle)

    #recent changes
    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())

    def set(self, ySpeed, xSpeed, zRotation, gyroAngle):
        self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)
