from translater.lag_code import *
from translater.char_spliter import *

def convert_to_kor(word, language):

    if language != 'japanese':
        phonemes = ipa_splitter(word)
        phonemes = [Phoneme(p[0], p[1], p[2]) for p in phonemes]

        if language == 'english':
            wor_c = EnglishCode(phonemes)
        elif language == 'portuguese':
            wor_c = PortugueseCode(phonemes)
        elif language == 'french':
            wor_c = FrenchCode(phonemes)
        elif language == 'spanish':
            wor_c = SpenishCode(phonemes)
        else:
            wor_c = CommonCode(phonemes)

        wor_c.localization()
        wor_c.gliding()
        wor_c.rounding()
        wor_c.nasalization()
        wor_c.make_syll()

    else:
        phonemes = jap_splitter(word)
        phonemes = [Phoneme(p[0], p[1], p[2]) for p in phonemes]
        wor_c = CommonCode(phonemes)

    return wor_c.combine_kor()