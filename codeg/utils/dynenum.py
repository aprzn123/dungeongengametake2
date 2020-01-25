class DynamicEnum:
    """Like an enum, but you can use anything as a keyword."""
    def __init__(self):
        self._n = 0

    def __getattr__(self, attr):
        setattr(self, attr, self._n)
        self._n += 1
        return self._n - 1

    def manual_add(self, attr):
        getattr(self, attr)

    def __repr__(self):
        d = {}
        for key, value in self.__dict__.items():
            if key != '_n':
                d[key] = value
        return str(d)

    def __str__(self):
        return self.__repr__()
