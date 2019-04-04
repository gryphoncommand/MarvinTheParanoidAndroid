from wpilib.encoder import Encoder

'''
    Inherents from wpilib.encoder.Encoder
'''
class Encoder(Encoder):

    def __init__(self, dio_in, dio_out, inverted=False):
        super().__init__(dio_in, dio_out, inverted,
                           Encoder.EncodingType.k4X)
    def useDistance(self):
        self.setPIDSourceType(Encoder.PIDSourceType.kDisplacement)

    def useRate(self):
        self.setPIDSourceType(Encoder.PIDSourceType.kRate)