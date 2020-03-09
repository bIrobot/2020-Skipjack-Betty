import rev
import wpilib
from magicbot import StateMachine, state, timed_state


class Climb(StateMachine):
    '''
        Climb Mechanism
    '''

    RLSparkMax: rev.CANSparkMax # climb winch motor
    
    @state(first=True)
    def nothing(self):
        self.RLSparkMax.set(0)
