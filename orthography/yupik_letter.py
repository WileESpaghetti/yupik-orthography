#!python
#encoding utf-8
import orthography


class YupikLetter(orthography.YupikChar):
    """
    add pronounciation info and alphebetical context to YupikChars
    """

    def __init__(self, c):
        super(YupikLetter, self).__init__(c)

    def is_vowel(self):
        pass

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