

class BasicOption(object):
    def __int__(self, *args, **kwargs):
        super(BasicOption, self).__init__()
        self._data = kwargs

    def __setattr__(self, key, value):
        if '_Core__initialised' not in self.__dict__:
            return self.app.__setattr__(self, key, value)
        elif '_data' in self.__dict__ and key in self._data:
            self._data[key] = value
        else:
            return self.app.__setattr__(self, key, value)

    def __getattr__(self, item):
        try:
            return self.app.__getattribute__(item)
        except AttributeError:
            try:
                if '_data' in self.__dict__:
                    return self._data[item]
            except KeyError:
                raise AttributeError(item)

    @property
    def option(self):
        return self.app



    # def save_as(self, doc, file_path, as_copy=True, extension_type=2):
    #     """Saves the Document with the specified save options."""
    #     return doc.save_as(file_path, self, as_copy,
    #                        extension_type)
