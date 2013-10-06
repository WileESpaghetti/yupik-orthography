#!python
#encoding utf-8
import orthography


class YupikConsonant(orthography.YupikLetter):
    def __init__(self, c):
        # FIXME needs to thow exception if c is already a vowel
        super(YupikConsonant, self).__init__(c)
        self.__consonant = True

    def is_consonant(self):
        return True