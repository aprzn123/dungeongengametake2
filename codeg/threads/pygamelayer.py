import pygame

from codeg.pygamelayer.instructionlayer import instl
from codeg.pygamelayer.eventlayer import evl
from codeg.datashare.gamequit import game_quit
from codeg.enums.instructions import Instructions

def pygame_layer():
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            else:
                evl.put_event(event)
        
        ni = instl.grab_inst() # next instruction
        
        ret_val = None
        args = ni.args
        inst = ni.inst

        # long if statement do do different things depending on the instruction given.
        if inst == Instructions.BLIT:
            args["onto"].blit(args["onfrom"], args["coords"])
        elif inst == Instructions.NEW_SURFACE:
            ret_val = pygame.Surface(args["size"])

        ni.resolve(ret_val)

        # direct events to destinations
        evl.direct_events()

        if game_quit:
            pygame.quit()
            break
    