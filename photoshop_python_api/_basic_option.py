

class BasicOption(object):
    def __int__(self, *args, **kwargs):
        self._data = kwargs

    def __setattr__(self, key, value):
        try:
            self._data.update({key: value})
            return object.__setattr__(self, key, value)
        except RuntimeError:
            return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        try:
            return self.__getattribute__(item)
        except AttributeError:
            return self._data.get(item)

    @property
    def option(self):
        return self.app
