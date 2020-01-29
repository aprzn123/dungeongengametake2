from codeg.enums.instructions import Instructions
from codeg.pygamelayer.instructionlayer import instl
from pygame import locals as pglocals

class Display:
    def __init__(self, size, flags):
        self.window = instl.run_inst(Instructions.NEW_WINDOW, 
                                     {"size": size, "flags": flags})

    def blit(self, surface, coords):
        instl.fast_run_inst(Instructions.BLIT, {"onfrom": surface, "onto": self, "coords": coords})

display = Display((0, 0), pglocals.FULLSCREEN)