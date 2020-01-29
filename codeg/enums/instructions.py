from enum import Enum

class Instructions(Enum):
    BLIT = 1
    NEW_SURFACE = 2
    NULL_INST = 3
    LOAD_IMAGE = 4
    NEW_WINDOW = 5