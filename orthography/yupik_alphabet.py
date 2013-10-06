#!python
#encoding utf-8
import orthography


class YupikAlphabet(object):
    def __init__(self):
        # the 18 official letters
        self.__alphabet = {
            u'a': orthography.YupikChar(u'a'),
            u'c': orthography.YupikChar(u'c'),
            u'e': orthography.YupikChar(u'e'),
            u'g': orthography.YupikChar(u'g'),
            u'i': orthography.YupikChar(u'i'),
            u'k': orthography.YupikChar(u'k'),
            u'l': orthography.YupikChar(u'l'),
            u'm': orthography.YupikChar(u'm'),
            u'n': orthography.YupikChar(u'n'),
            u'p': orthography.YupikChar(u'p'),
            u'q': orthography.YupikChar(u'q'),
            u'r': orthography.YupikChar(u'r'),
            u's': orthography.YupikChar(u's'),
            u't': orthography.YupikChar(u't'),
            u'u': orthography.YupikChar(u'u'),
            u'v': orthography.YupikChar(u'v'),
            u'w': orthography.YupikChar(u'w'),
            u'y': orthography.YupikChar(u'y'),
        }
