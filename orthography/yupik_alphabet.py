#!python
#encoding utf-8
import orthography


class YupikAlphabet(object):
    def __init__(self):
        # the 18 official letters
        self.__alphabet = {
            u'a': orthography.YupikVowel(u'a'),
            u'c': orthography.YupikConsonant(u'c'),
            u'e': orthography.YupikVowel(u'e'),
            u'g': orthography.YupikConsonant(u'g'),
            u'i': orthography.YupikVowel(u'i'),
            u'k': orthography.YupikConsonant(u'k'),
            u'l': orthography.YupikConsonant(u'l'),
            u'm': orthography.YupikConsonant(u'm'),
            u'n': orthography.YupikConsonant(u'n'),
            u'p': orthography.YupikConsonant(u'p'),
            u'q': orthography.YupikConsonant(u'q'),
            u'r': orthography.YupikConsonant(u'r'),
            u's': orthography.YupikConsonant(u's'),
            u't': orthography.YupikConsonant(u't'),
            u'u': orthography.YupikVowel(u'u'),
            u'v': orthography.YupikConsonant(u'v'),
            u'w': orthography.YupikConsonant(u'w'),
            u'y': orthography.YupikConsonant(u'y'),
        }
