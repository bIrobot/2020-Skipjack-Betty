import wpilib
from magicbot import AutonomousStateMachine, state, timed_state


class DoNothing(AutonomousStateMachine):

    MODE_NAME = "Do Nothing"
    DEFAULT = True                                                                         

    @state(first=True)
    def stop(self):
        pass
