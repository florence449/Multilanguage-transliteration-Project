ipa_vowels_map = {
    1: {
        'a': 'ㅏ', 'e': 'ㅔ', 'i': 'ㅣ', 'o': 'ㅗ', 'u': 'ㅜ',
        'ʌ': 'ㅓ', 'ɔ': 'ㅗ', 'ɑ': 'ㅏ', 'ə': 'ㅓ', 'ɪ': 'ㅣ',
        'ʊ': 'ㅜ', 'æ': 'ㅐ', 'ɛ': 'ㅔ', 'y': 'ㅟ', 'ø': 'ㅚ',
        'œ': 'ㅚ', 'ɐ':'ㅏ', 'ʏ':'ㅟ', 'ĩ':'ㅣ', 'ẃ':'ㅜ',
        'w': 'ㅜ', 'j': 'ㅣ', 'ɚ':'ㅓ', 'ɜ':'ㅓ', 'ä':'ㅏ', 'ɒ':'ㅏ'
    },
    2: {
        'ɐ̯':'ㅏ', 'ɪ̯':'ㅣ',
        'ɑ̃':'ㅏ', 'ɛ̃':'ㅐ', 'ɔ̃':'ㅗ',
        'œ̃':'ㅚ', 'ĩ':'ㅣ', 'ũ':'ㅜ',
        'õ':'ㅗ', 'ɐ̃':'ㅏ', 'ɯᵝ':'ㅜ',
        'oʊ': 'ㅗ', 'yi':'ㅟ', 'uw':'ㅜ', 'əʊ':'ㅗ',
        'ou': 'ㅗ'
    },
    3: {
        '̯̈f':'ㅣ', 'jja':'ㅑ', 'jje':'ㅖ'
    },
    4: {'ɐ̃w̃':['ㅏ','ㅇ'], 'ɐ̃ʊ̃':'ㅏ'}
}

ipa_consonants_map = {
    1: {
        'p': 'ㅍ', 'b': 'ㅂ', 't': 'ㅌ', 'd': 'ㄷ', 'k': 'ㅋ', 'g': 'ㄱ',
        'f': 'ㅍ', 'v': 'ㅂ', 'θ': 'ㅅ', 'ð': 'ㄷ', 's': 'ㅅ', 'z': 'ㅈ', 'h': 'ㅎ',
        'ç': 'ㅎ', 'x': 'ㅎ', 'ɣ': 'ㄱ', 'ʁ': 'ㄹ', 'χ': 'ㅎ', 'ħ': 'ㅎ',
        'm': 'ㅁ', 'n': 'ㄴ', 'ŋ': 'ㅇ', 'l': 'ㄹ',
        'r': 'ㄹ', 'ɾ': 'ㄹ', 'ɹ': 'ㄹ', 'ɡ':'ㄱ',
        'ʃ':'ㅅ', 'ʂ':'ㅅ', 'ʒ':'ㅈ', 'ɲ':'ㄴ', 'ʀ':'ㄹ', 'ʝ':'ㅎ', 'ʤ':'ㅈ',
        'β':'ㅂ', 'ʑ':'ㅈ', 'ɭ':'ㄹ', 'ɦ':'ㅎ', 'ɕ':'ㅅ', 'ɽ':'ㄹ', 'ɴ':'ㄴ', 'ʎ':'ㄹ', '̃':'ㅇ'
    },
    2: {
        'pʰ': 'ㅍ', 'tʰ': 'ㅌ', 'kʰ': 'ㅋ', # 유기음
        'tʃ': 'ㅊ', 'dʒ': 'ㅈ', # 파찰음
        'ts': 'ㅊ', 'dz': 'ㅈ', # 파찰음
        'ʀʀ': 'ㄹ', 'ɾɾ': 'ㄹ', 'tɕ':'ㅊ'
    },
    3: {
        'ɲ': 'ㄴ',
        't͡ʃ': 'ㅊ',
        'd͡ʒ': 'ㅈ',
        'd͡ɮ': 'ㄷ',
        't͡s': 'ㅊ',
        'd͡z': 'ㅈ',
        't͡ɕ': 'ㅊ'
    }
}

syllabic_clusters_map = {
    1: {},
    2: {
        'm̩': '음', 'n̩': '은', 'l̩': '을', 'r̩': '르', 'ŋ̍': '응',
    },
    3: {
        't͡ɬ':'틀'
    }
}

def ipa_splitter(word):
    result = []
    i = 0

    while i < len(word):
        # 띄워쓰기
        if i + 1 <= len(word) and word[i] == ' ':
            result.append(['space', ' ', 'special'])
            i += 1

        # 4개 기호
        elif i + 4 <= len(word) and word[i:i+4] in ipa_vowels_map.get(4, {}):
            result.append([word[i:i+4], ipa_vowels_map[4][word[i:i+4]], 'vowel'])
            i += 4

        # 3개 기호
        elif i + 3 <= len(word) and word[i:i+3] in ipa_vowels_map.get(3, {}):
            result.append([word[i:i+3], ipa_vowels_map[3][word[i:i+3]], 'vowel'])
            i += 3

        elif i + 3 <= len(word) and word[i:i+3] in ipa_consonants_map.get(3, {}):
            result.append([word[i:i+3], ipa_consonants_map[3][word[i:i+3]], 'consonant'])
            i += 3

        elif i + 3 <= len(word) and word[i:i+3] in syllabic_clusters_map.get(3, {}):
            result.append([word[i:i+3], syllabic_clusters_map[3][word[i:i+3]], 'syllabic'])
            i += 3

        # 2개 기호
        elif i + 2 <= len(word) and word[i:i+2] in ipa_vowels_map.get(2, {}):
            result.append([word[i:i+2], ipa_vowels_map[2][word[i:i+2]], 'vowel'])
            i += 2

        elif i + 2 <= len(word) and word[i:i+2] in ipa_consonants_map.get(2, {}):
            result.append([word[i:i+2], ipa_consonants_map[2][word[i:i+2]], 'consonant'])
            i += 2

        elif i + 2 <= len(word) and word[i:i+2] in syllabic_clusters_map.get(2, {}):
            result.append([word[i:i+2], syllabic_clusters_map[2][word[i:i+2]], 'syllabic'])
            i += 2

        # 1개의 기호
        elif i + 1 <= len(word) and word[i] in ipa_vowels_map.get(1, {}):
            result.append([word[i], ipa_vowels_map[1][word[i]], 'vowel'])
            i += 1

        elif i + 1 <= len(word) and word[i] in ipa_consonants_map.get(1, {}):
            result.append([word[i], ipa_consonants_map[1][word[i]], 'consonant'])
            i += 1

        elif i + 1 <= len(word) and word[i] in syllabic_clusters_map.get(1, {}):
            result.append([word[i], syllabic_clusters_map[1][word[i]], 'syllabic'])
            i += 1

        # 사용하지 않는 문자를 건너뜀
        elif i + 1 <= len(word) and word[i] in ('ː'):
            i += 1


        #5. 처리되지 않는 문자에 대하여 오류 확인
        else:
            print(f"{word[i]} is not found on phoneme dictionary")
            i += 1 # 처리되지 않은 문자도 건너뛰어야 무한 루프에 빠지지 않습니다.

    return result