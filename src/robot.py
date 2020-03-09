# !/usr/bin/env python3

import ctre
import magicbot
import navx
import rev
import wpilib
import wpilib.drive
from networktables import NetworkTables

import components.climb
import components.drivetrain
import components.power_cell_handler
import components.wheel_of_fortune


class MyRobot(magicbot.MagicRobot):
    climb: components.climb.Climb
    drivetrain: components.drivetrain.Drivetrain
    power_cell_handler: components.power_cell_handler.Power_Cell_Handler
    wheel_of_fortune: components.wheel_of_fortune.Wheel_Of_Fortune

    def createObjects(self):
        """Robot initialization function"""

        # Initialize motor controllers
        self.frontLeftMotor = ctre.WPI_TalonFX(1)
        self.frontRightMotor = ctre.WPI_TalonFX(2)
        self.rearLeftMotor = ctre.WPI_TalonFX(3)
        self.rearRightMotor = ctre.WPI_TalonFX(4)
        self.FLSparkMax = rev.CANSparkMax(5, rev.CANSparkMaxLowLevel.MotorType(1))
        self.FRSparkMax = rev.CANSparkMax(6, rev.CANSparkMaxLowLevel.MotorType(1))
        self.RLSparkMax = rev.CANSparkMax(7, rev.CANSparkMaxLowLevel.MotorType(1))
        self.RRSparkMax = rev.CANSparkMax(8, rev.CANSparkMaxLowLevel.MotorType(1))
        self.FLTalon = ctre.WPI_TalonSRX(9)
        self.FRTalon = ctre.WPI_TalonSRX(10)
        self.RLTalon = ctre.WPI_TalonSRX(11)
        self.RRTalon = ctre.WPI_TalonSRX(12)
        self.LVictor = ctre.WPI_VictorSPX(13)
        self.RVictor = ctre.WPI_VictorSPX(14)

        # Initialize switches and hall-effect sensors
        self.limit_switch = wpilib.DigitalInput(0)

        # Configure drive object
        self.left = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.right = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightMotor)
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

        # Initialize controller
        self.controller = wpilib.XboxController(0)

        wpilib.CameraServer.launch()

        NetworkTables.initialize()
        self.sd = NetworkTables.getTable("SmartDashboard")

        # Communicate w/navX MXP via the MXP SPI Bus.
        # - Alternatively, use the i2c bus.
        # See http://navx-mxp.kauailabs.com/guidance/selecting-an-interface/ for details
        self.navxSensor = navx.AHRS.create_spi()
        # self.navxSensor = navx.AHRS.create_i2c()

    def teleopInit(self):
        """Executed at the start of teleop mode"""

        pass

    def teleopPeriodic(self):
        """Executed periodically during teleop mode"""

        self.drivetrain.move(self.controller.getY(self.controller.Hand(0)), self.controller.getX(self.controller.Hand(0)))
    
    def testInit(self):
        """Executed at the start of test mode"""

        pass

    def testPeriodic(self):
        """Executed periodically during test mode"""

        pass

    def disabledInit(self):
        """Executed at the start of disabled mode"""

        pass

    def disabledPeriodic(self):
        """Executed periodically during disabled mode"""

        pass

    def robotPeriodic(self):
        """Executed periodically at the end of every robot mode"""

        angle = self.navxSensor.getAngle()
        self.sd.putNumber('navx/yaw', self.navxSensor.getAngle())

        wpilib.SmartDashboard.updateValues()


if __name__ == "__main__":
    wpilib.run(MyRobot)
