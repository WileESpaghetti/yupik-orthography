#!python
#encoding utf-8
import orthography


class YupikConsnant(orthography.YupikLetter):
    def __init__(self, c):
        # FIXME needs to thow exception if c is already a vowel
        super(YupikConsnant, self).__init__(c)
        self.__consonant = True

    def is_consonant(self):
        return True