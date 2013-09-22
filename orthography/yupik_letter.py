#!python
#encoding utf-8
import orthography


class YupikLetter(orthography.YupikChar):
    def __init__(self, c):
        super(YupikLetter, self).__init__(c)
