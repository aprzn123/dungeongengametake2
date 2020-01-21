from code.utils.dynenum import DynamicEnum
from code.utils.exceptions import FinalizationException

state_names = DynamicEnum()
state_cases = DynamicEnum()

class State:
    def __init__(self, name, on_entering):
        self.name = name
        self.switch_map = {}
        self.on_entering = on_entering
    
    def add_connection(self, other, case):
        self.switch_map[case] = other

    def get_node(case):
        return self.switch_map[case]


class FiniteStateMachine:
    def __init__(self):
        self.states = {}
        self.final = False
        self.state = None

    def add_state(self, state):
        if self.final:
            raise FinalizationException('The FSM has been finalized and thus can no longer be changed')
        else:
            self.states[state.name] = state

    def finalize(self, starting_state):
        self.final = True
        self.state = starting_state

    def update(self, case):
        if self.final:
            self.state = self.state.get_node(case)
            self.state.on_entering()
        else:
            raise FinalizationException('The FSM cannot be used before finalization')

    def get_cases(self):
        if self.final:
            return list(self.state.states.keys())
        else:
            raise FinalizationException('The FSM cannot be used before finalization')
