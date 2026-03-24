from translater.lag_code import *
from translater.char_spliter import *
from logger import get_logger

logger = get_logger(__name__)

def convert_to_kor(word, language):

    if language != 'japanese':
        phonemes = ipa_splitter(word)
        phonemes = [Phoneme(p[0], p[1], p[2]) for p in phonemes]

        if language == 'english':
            word_con = EnglishCode(phonemes)
        elif language == 'portuguese':
            word_con = PortugueseCode(phonemes)
        elif language == 'french':
            word_con = FrenchCode(phonemes)
        elif language == 'spanish':
            word_con = SpenishCode(phonemes)
        else:
            word_con = CommonCode(phonemes)

        word_con.localization()
        word_con.gliding()
        word_con.rounding()
        word_con.nasalization()
        word_con.make_syll()
        logger.info(word_con.syllables)

    else:
        phonemes = jap_splitter(word)
        phonemes = [Phoneme(p[0], p[1], p[2]) for p in phonemes]
        word_con = CommonCode(phonemes)
        logger.info(word_con.phonemes)

    result = word_con.combine_kor()

    logger.info(result)

    return result