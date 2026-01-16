import pandas as pd
from fn_spliter.ipa_splitter import ipa_splitter
from fn_spliter.jap_splitter import jap_splitter
from word_class.main_class import *
from word_class.en_word_class import *
from word_class.fr_word_class import *
from word_class.es_word_class import *
from word_class.pr_word_class import *

def convert_to_kor(word, language):

    language_dict = {
        1:'english',
        2:'portuguese',
        3:'french',
        4:'spanish',
        5:'germanian',
        6:'italian',
        7:'russian',
        8:'norwegian',
        9: 'caribbean',
        10: 'nahuatl',
        11: 'mayan',
        12: 'haitian',
        13: 'japanese'
    }

    if language_dict[language] != 'japanese':
        phonemes = ipa_splitter(word)
        phonemes = [Phoneme(p[0], p[1], p[2]) for p in phonemes]

        if language_dict[language] == 'english':
            wor_c = EnWord(phonemes)
        elif language_dict[language] == 'portuguese':
            wor_c = PrWord(phonemes)
        elif language_dict[language] == 'french':
            wor_c = FrWord(phonemes)
        elif language_dict[language] == 'spanish':
            wor_c = EsWord(phonemes)
        else:
            wor_c = Word(phonemes)

        wor_c.localization()
        wor_c.gliding()
        wor_c.rounding()
        wor_c.nasalization()
        wor_c.make_syll()

    else:
        phonemes = jap_splitter(word)
        phonemes = [Phoneme(p[0], p[1], p[2]) for p in phonemes]
        wor_c = Word(phonemes)

    return wor_c.combine_kor()
