from codeg.utils.dynenum import DynamicEnum
from codeg.utils.exceptions import FinalizationException

# state_names
sn = DynamicEnum()
# state_cases
sc = DynamicEnum()

class State:
    def __init__(self, name, on_entering, on_exiting):
        self.name = name
        self.switch_map = {}
        self.on_entering = on_entering
        self.on_exiting = on_exiting
    
    def add_connection(self, other, case):
        self.switch_map[case] = other

    def get_node(self, case):
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
        self.state = self.states[starting_state]
        self.state.on_entering()

    def update(self, case):
        if self.final:
            self.state.on_exiting()
            self.state = self.state.get_node(case)
            self.state.on_entering()
        else:
            raise FinalizationException('The FSM cannot be used before finalization')

    def get_cases(self):
        if self.final:
            return list(self.state.switch_map.keys())
        else:
            raise FinalizationException('The FSM cannot be used before finalization')
