class enum(object):
    def __init__(self, *args, **kwargs):
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])
