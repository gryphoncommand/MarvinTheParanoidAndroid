from enum import Enum

class InfoPasser:
    """
    Dummy class used to store variables on an object.
    """
    pass

axes = InfoPasser()

axes.L_x = 0
axes.L_y = 1

axes.R_x = 2
axes.R_y = 5
#pip3 install --upgrade robotpy-navx

# triggers
axes.L_t = 3
axes.R_t = 4

axes.motor_inversion = [-1,1,1]


class NavXType(Enum):

    I2C = 1
    SPI = 2

navx_type = NavXType.SPI