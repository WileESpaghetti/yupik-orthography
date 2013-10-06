#!python
#encoding utf-8
import orthography


class YupikLetter(orthography.YupikChar):
    """
    add pronounciation info and alphebetical context to YupikChars
    """

    def __init__(self, c):
        super(YupikLetter, self).__init__(c)

        if isinstance(c, YupikLetter):
            self.__pronunciation = c
        else:
            self.__pronunciation = None

        # default letter types
        self.__vowel = None
        self.__prime_vowel = None
        self.__consonant = None
        self.__symbol = None
        self.__valid = None

        # letter classes
        self.__stop = None
        self.__fricative = None
        self.__nasal = None

        self.__labial = None
        self.__velar = None
        self.__apical = None

        # default pronounciation
        self.__voicing = None
        self.__gemination = None
        self.__auto_gemination = None
        self.__rhythmic_length = None
        self.__stress = None


    def is_vowel(self):
        is_vowel = self.__vowel
        if self.__pronunciation:
            is_vowel = self.__pronunciation.is_vowel()

        return is_vowel

    def is_prime_vowel(self):
        pass

    def is_consonant(self):
        pass

    def is_symbol(self):
        pass

    def is_valid(self):
        pass

    ### Manner of articulation ###

    def is_stop(self):
        pass

    def is_fricative(self):
        pass

    def is_nasal(self):
        pass

    ### Place of articulation ###

    def is_labial(self):
        pass

    def is_velar(self):
        pass

    def is_apical(self):
        pass

    ### Pronounciation ###

    def is_voiced(self):
        pass

    def has_gemination(self):
        pass

    # XXX: this might be useful for syllables too
    def has_rhythmic_length(self):
        pass

    # XXX: this might be useful for syllables too
    def has_stress(self):
       pass