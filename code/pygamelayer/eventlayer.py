from queue import Queue

from pygame.locals import *

from code.enums.events import Events
from code.datashare import gamequit

class Event:
    def __init__(self, event):
        # TODO: Make this interpret pygame event
        try:
            self.ev = {
                ACTIVEEVENT: Events.ACTIVEEVENT,
                KEYDOWN: Events.KEYDOWN,
                KEYUP: Events.KEYUP,
                MOUSEMOTION: Events.MOUSEMOTION,
                MOUSEBUTTONDOWN: Events.MOUSEBUTTONDOWN,
                MOUSEBUTTONUP: Events.MOUSEBUTTONUP,
                JOYAXISMOTION: Events.JOYAXISMOTION,
                JOYBALLMOTION: Events.JOYBALLMOTION,
                JOYHATMOTION: Events.JOYHATMOTION,
                JOYBUTTONDOWN: Events.JOYBUTTONDOWN,
                JOYBUTTONUP: Events.JOYBUTTONUP,
                VIDEORESIZE: Events.VIDEORESIZE,
                VIDEOEXPOSE: Events.VIDEOEXPOSE,
                USEREVENT: Events.USEREVENT
            }[event.type]
        except:
            print(f'ERROR: EVENT OF TYPE {event.type} NOT RECOGNIZED')
            gamequit.game_quit = True
        self.args = None

class EventLayer:
    def __init__(self):
        events = Queue()
    
    def put_event(self, event):
        self.events.put(Event(event))

evl = EventLayer()