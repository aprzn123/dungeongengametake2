from queue import Queue

from pygame.locals import *

from code.enums.events import Events
from code.datashare import gamequit
from code.inputhandling.intakequeue import eiq

class Event:
    def __init__(self, event):
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
        except KeyError:
            print(f'FATAL: EVENT OF TYPE {event.type} NOT RECOGNIZED')
            gamequit.game_quit = True
        self.args = {}

        ev = self.ev

        if ev == Events.ACTIVEEVENT:
            args = {'gain': event.gain, 'state': event.state}
        elif ev == Events.KEYDOWN:
            args = {'key': event.key, 'mod': event.mod, 'unicode': event.unicode, 'scancode': event.scancode}
        elif ev == Events.KEYUP:
            args = {'key': event.key, 'mod': event.mod}
        elif ev == Events.MOUSEMOTION:
            args = {'pos': event.pos, 'rel': event.rel, 'buttons': event.buttons}
        elif ev == Events.MOUSEBUTTONDOWN:
            args = {'pos': event.pos, 'button': event.button}
        elif ev == Events.MOUSEBUTTONUP:
            args = {'pos': event.pos, 'button': event.button}
        elif ev == Events.JOYAXISMOTION:
            pass
        elif ev == Events.JOYBALLMOTION:
            pass
        elif ev == Events.JOYHATMOTION:
            pass
        elif ev == Events.JOYBUTTONDOWN:
            pass
        elif ev == Events.JOYBUTTONUP:
            pass
        elif ev == Events.VIDEORESIZE:
            args == {'size': event.size, 'w': event.w, 'h': event.h}


class EventLayer:
    def __init__(self):
        events = Queue()
    
    def put_event(self, event):
        self.events.put(Event(event))

    def direct_event(self):
        event = self.events.get()
        ev = event.ev
        if ev == Events.ACTIVEEVENT:
            pass
        elif ev == Events.KEYDOWN:
            pass
        elif ev == Events.KEYUP:
            pass
        elif ev == Events.MOUSEMOTION:
            pass
        elif ev == Events.MOUSEBUTTONDOWN:
            pass
        elif ev == Events.MOUSEBUTTONUP:
            pass
        elif ev == Events.JOYAXISMOTION:
            pass
        elif ev == Events.JOYBALLMOTION:
            pass
        elif ev == Events.JOYHATMOTION:
            pass
        elif ev == Events.JOYBUTTONDOWN:
            pass
        elif ev == Events.JOYBUTTONUP:
            pass
        elif ev == Events.VIDEORESIZE:
            pass
    
    def direct_events(self):
        pass


evl = EventLayer()