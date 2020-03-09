import wpilib
import wpilib.drive


class Drivetrain:
    '''
        Robot Drivetrain
    '''

    drive: wpilib.drive.DifferentialDrive

    def __init__(self):
        self.enabled = True
        self.speed = 0
        self.rotation = 0

    def enable(self, value):
        self.enabled = value
    
    def move(self, speed, rotation):
        self.speed = speed
        self.rotation = rotation
    
    def execute(self):
        if self.enabled:
            self.drive.arcadeDrive(self.speed, self.rotation, True)
        else:
            self.drive.arcadeDrive(0, 0, True)
