from phonemizer import phonemize
from cyrtranslit import to_cyrillic

def ipa_converter(word, language):
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
    return result