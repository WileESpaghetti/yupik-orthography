#!python
#encoding utf-8


class YupikChar(object):
    def __init__(self, c):
        self.ychar = repr(c)

    def __copy__(self):
        return YupikChar(self.ychar)

    def __str__(self):
        return self.ychar

    def __repr__(self):
        return self.ychar

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

