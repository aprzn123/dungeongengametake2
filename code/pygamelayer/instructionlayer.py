from queue import Queue, Empty

from code.enums.instructions import Instructions

class Instruction:
    def __init__(self, inst, args):
        """Initializes an instruction. Marks it uncompleted, 
        initializes a return value, and assigns other variables.
        
        Arguments:
            inst {code.enums.instructions.Instructions} -- Instruction
            args {dict} -- Arguments given to the instruction
        """        
        self.inst = inst
        self.args = args
        self.complete = False
        self.ret_val = None

    def resolve(self, ret_val):
        """Resolves instruction by giving a return value and marking complete
        
        Arguments:
            ret_val {any} -- Return value
        """        
        self.ret_val = ret_val
        self.complete = True

    def return_(self):
        """Access return value of the function
        
        Returns:
            any -- Return value of the instruction
        """        
        return ret_val


class InstructionLayer:
    """InstructionLayer is a way to access Pygame instructions so all 
    pygame functions can be executed in one thread. 
    """    
    def __init__(self):
        """Initializes a queue for storing incoming instructions.
        """        
        self.instructions = Queue()
    
    def new_inst(self, inst):
        """Adds a new instruction to the queue and gives it
        an id for internal use.
        
        Arguments:
            inst {code.pygamelayer.instructionlayer.Instruction} -- Instruction to be added
        """
        self.instructions.put(inst)

    def grab_inst(self):
        try:
            inst = self.instructions.get_nowait()
        except Empty:
            inst = Instruction(Instructions.NULL_INST, {})
        return inst

    def run_inst(self, inst, args):
        """Runs given instruction with given args and returns its return value.
        
        Arguments:
            inst {code.enums.instructions.Instructions} -- enum for which instruction to be executed
            args {dict} -- arguments passed to instruction
        
        Returns:
            any -- return value of instruction
        """        
        tbr = Instruction(inst, args) # tbr stands for "to be run"
        self.new_inst(tbr)
        while not tbr.complete:
            pass
        return tbr.return_()

    def fast_run_inst(self, inst, args):
        """Runs instruction with given args without returning anything.
        
        Arguments:
            inst {code.enums.instructions.Instructions} -- enum for which instruction to be executed
            args {dict} -- arguments passed to instruction
        """        
        tbr = Instruction(inst, args) # again, tbr stands for "to be run"
        self.new_inst(tbr)

instl = InstructionLayer()
