import ctre
import rev
import wpilib


class Power_Cell_Handler:
    '''
        Power Cell Handler
    '''

    FLSparkMax: rev.CANSparkMax # upper drive motor
    FRSparkMax: rev.CANSparkMax # lower drive motor
    FLTalon: ctre.WPI_TalonSRX # ratchet strap motor

    def __init__(self):
        self.enabled = True
        self.eject_toggle = False
        self.belt_speed = 0

    def enable(self, value):
        self.enabled = value

    def toggle_position(self):
        if self.eject_toggle:
            self.eject_toggle = False
        else:
            self.eject_toggle = True

    def drive_belts(self, value):
        self.belt_speed = value

    def execute(self):
        if self.enabled:
            self.FLSparkMax.set(self.belt_speed)
            self.FRSparkMax.set(self.belt_speed * -1)
        else:
            self.FLSparkMax.set(0)
            self.FRSparkMax.set(0)
