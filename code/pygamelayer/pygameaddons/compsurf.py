from code.pygamelayer.instructionlayer import instl
from code.enums.instructions import Instructions

class CompositeSurface:
    def __init__(self, surfaces, size):
        """Initializes a Composite Surface
        
        Arguments:
            surfaces {list} -- A list of iterables each with a Surface and coordinates for that surface
            size {tuple} -- A tuple with the of the surface
        """
        self.size = size
        self.surfaces = []
        for surface in surfaces:
            self.surfaces.append(surface)
        self.base_surface = instl.run_inst(
            Instructions.NEW_SURFACE, 
            {
                "size": self.size
            }
        )
        self.base_surface.convert()
        
        self.update()

    def update(self):
        for surface, coords in self.surfaces:
            instl.fast_run_inst(
                Instructions.BLIT, 
                {
                    "onfrom": surface, 
                    "onto": self.base_surface, 
                    "coords": coords
                }
            )
    def get_surface(self):
        return self.base_surface