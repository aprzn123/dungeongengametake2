from queue import Queue

class EventIntakeQueue:
    def __init__(self):
        self.events_in = Queue()

    def add_event(self, event):
        self.events_in.put(event)

    def get_event(self):
        return self.events_in.get()

eiq = EventIntakeQueue()