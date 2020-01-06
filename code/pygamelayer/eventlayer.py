from queue import Queue

class Event:
    def __init__(self, event):
        # TODO: Make this interpret pygame event
        self.ev = None
        self.args = None

class EventLayer:
    def __init__(self):
        events = Queue()
    
    def put_event(self, event):
        self.events.put(Event(event))

evl = EventLayer()