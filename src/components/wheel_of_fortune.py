import ctre
import wpilib


class Wheel_Of_Fortune:
    '''
        Wheel Of Fortune
    '''

    FRTalon: ctre.WPI_TalonSRX # lift motor
    RLTalon: ctre.WPI_TalonSRX # spinner motor

    def __init__(self):
        self.enabled = True

    def enable(self, value):
        self.enabled = value

    def execute(self):
        '''This gets called at the end of the control loop'''
        if self.enabled:
            self.FRTalon.set(1)
            self.RLTalon.set(1)
        else:
            self.FRTalon.set(0)
            self.RLTalon.set(0)
