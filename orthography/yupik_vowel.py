#!python
#encoding utf-8
import orthography


class YupikVowel(orthography.YupikLetter):
    def __init__(self, c):
        # FIXME needs to thow exception if c is already a consonant
        super(YupikVowel, self).__init__(c)
        self.__vowel = True

    def is_vowel(self):
        return True