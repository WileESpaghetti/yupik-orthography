#!python
#encoding utf-8
from orthography import YupikChar

class YupikAlphabet(object):
    def __init__(self):
        # the 18 official letters
        self.__alphabet = {
            u'a': YupikChar(u'a'),
            u'c': YupikChar(u'c'),
            u'e': YupikChar(u'e'),
            u'g': YupikChar(u'g'),
            u'i': YupikChar(u'i'),
            u'k': YupikChar(u'k'),
            u'l': YupikChar(u'l'),
            u'm': YupikChar(u'm'),
            u'n': YupikChar(u'n'),
            u'p': YupikChar(u'p'),
            u'q': YupikChar(u'q'),
            u'r': YupikChar(u'r'),
            u's': YupikChar(u's'),
            u't': YupikChar(u't'),
            u'u': YupikChar(u'u'),
            u'v': YupikChar(u'v'),
            u'w': YupikChar(u'w'),
            u'y': YupikChar(u'y'),
        }
