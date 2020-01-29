from codeg.pygamelayer.instructionlayer import instl
from codeg.enums.instructions import Instructions
from codeg.utils.exceptions import FinalizationException
from codeg.display import display
from codeg.utils.parseconfig import config_cfg

class GameObject:
    def __init__(self, texture_uri):
        self.texture_uri = texture_uri
        self._texture = None

    def load_texture(self):
       self._texture = instl.run_inst(Instructions.LOAD_IMAGE, {"uri": self.texture_uri})

    @property
    def texture(self):
        if self._texture is None:
            raise FinalizationException("Texture has not yet loaded")
        else:
            return self._texture

    def render(self, x, y):
        display.blit(self.texture, (x, y))

class WorldObject(GameObject):
    def __init__(self, texture_uri, xpos, ypos):
        super().__init__(texture_uri)
        self.xpos = xpos
        self.ypos = ypos

    def render(self):
        super().render(self.xpos * config_cfg.data.DISPLAY.TileWidth, 
                       self.ypos * config_cfg.data.DISPLAY.TileWidth)