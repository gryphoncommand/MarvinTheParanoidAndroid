from enum import Enum


class InfoPasser:
    """
    Dummy class used to store variables on an object.
    """

    pass


axes = InfoPasser()

axes.L_x = 2
axes.L_y = 1

axes.R_x = 0
axes.R_y = 5
# pip3 install --upgrade robotpy-navx

# triggers
axes.L_t = 3
axes.R_t = 4

axes.motor_inversion = [-1, 1, 1]


class NavXType(Enum):

    I2C = 1
    SPI = 2


navx_type = NavXType.SPI

config = InfoPasser()
config.centric = True

# Motors
motors = InfoPasser()

motors.lf = 1
motors.lr = 2
motors.rf = 3
motors.rr = 4


# Encoders

encoders = InfoPasser()

# Agrs(port, port, inverted?)
encoders.lf = 0, 1, False
encoders.lr = 2, 3, True
encoders.rf = 4, 5, False
encoders.rr = 6, 7, True
