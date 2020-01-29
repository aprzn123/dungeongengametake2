import pygame

from codeg.pygamelayer.instructionlayer import instl
from codeg.pygamelayer.eventlayer import evl
from codeg.datashare.gamequit import game_quit
from codeg.enums.instructions import Instructions
from codeg.pygamelayer.pygameaddons.gsurf import GSurface

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
            ret_val = GSurface(args["size"])
        elif inst == Instructions.LOAD_IMAGE:
            ret_val = pygame.image.load(args["uri"]).convert()
        elif inst == Instructions.NEW_WINDOW:
            ret_val = pygame.display.set_mode(args["size"], args["flags"])

        ni.resolve(ret_val)

        # direct events to destinations
        evl.direct_events()

        if game_quit:
            pygame.quit()
            break
    