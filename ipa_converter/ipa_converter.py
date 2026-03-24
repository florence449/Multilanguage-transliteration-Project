from phonemizer import phonemize
from cyrtranslit import to_cyrillic
from logger import get_logger

logger = get_logger(__name__)

def ipa_converter(word, language):
    result = None  # 기본값 설정
    try:
        if language == 'english':
            result = phonemize(word, language='en-gb-x-rp', backend='espeak', njobs=1)
        elif language == 'portuguese':
            result = phonemize(word, language='pt-br', backend='espeak', njobs=1)
        elif language == 'french':
            result = phonemize(word, language='fr-fr', backend='espeak', njobs=1)
        elif language == 'spanish':
            result = phonemize(word, language='es-419', backend='espeak', njobs=1)
        elif language == 'norwegian':
            result = phonemize(word, language='nb', backend='espeak', njobs=1)
        elif language == 'germanian':
            result = phonemize(word, language='de', backend='espeak', njobs=1)
        elif language == 'italian':
            result = phonemize(word, language='it', backend='espeak', njobs=1)
        elif language == 'russian':
            result = phonemize(to_cyrillic(word, 'ru'), language='ru', backend='espeak', njobs=1)
        elif language == 'caribbean':
            result = phonemize(word, language='en-029', backend='espeak', njobs=1)
        elif language == 'nahuatl':
            result = phonemize(word, language='nci', backend='espeak', njobs=1)
        elif language == 'mayan':
            result = phonemize(word, language='quc', backend='espeak', njobs=1)
        elif language == 'haitian':
            result = phonemize(word, language='ht', backend='espeak', njobs=1)
        logger.info(f"language : {language} result: {result}")

    except Exception as e:
        logger.error(f"에러 발생 - language: {language}, word: {word}, error: {e}")

    return result