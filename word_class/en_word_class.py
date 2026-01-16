from word_class.main_class import *
from word_class.phoneme_context_class import *

class EnWord(Word):
    """
    영어 음운변화를 반영하는 메스드의 집합입니다.
    """
    gliding_consonant = {'ʃ', 'ʂ', 'ʝ', 'ɲ'}
    def localization(self):

        final_phoneme_dict = {
            'ㅍ':'ㅂ', 'ㅋ':'ㄱ', 'ㅌ':'ㅅ'
        }

        short_vowel = ['ɪ', 'e', 'æ', 'ʌ', 'ɒ', 'ʊ', 'ə', 'a', 'ɪ_JC']

        output_phoneme_list = []

        for i, phoneme in enumerate(self.phonemes):

            c = PhonemeContext(self.phonemes, i)

            # 1항 무성 파열음
            if (
                phoneme.code in ('p', 't', 'k')
                and (
                        ## 짧은 모음 뒤
                        (self.phonemes[i-1].code in short_vowel and not c.is_two_prev_vowel())
                        and (
                            ## 어말의 무성파열음(p, k, t)는 받힘으로 적는다.
                            c.is_end_of_word()
                            ## 짧은 모음과 유음·비음(l, r, m, n) 이외의 자음 사이에 오는 무성 파열음(p, t, k)은 받침으로 적는다.
                            or (c.is_next_consonant() and not self.phonemes[i-1].code in ('l', 'ɭ', 'n', 'm', 'r'))
                        )
                    )
                ):
                output_phoneme_list.append(Phoneme(f"FC_{phoneme.code}", final_phoneme_dict[phoneme.kor_code], phoneme.type))

            # 2항 유성 파열음
            ## 어말과 모든 자음 앞에 오는 유성 파열음은 '으'를 붙여 적는다.
            ### 받힘 가능 음소로 코딩

            # 제3항 마찰음
            ## 어말과 모든 자음 앞에 오는 마찰음은 '으'를 붙여 적는다.
            ### 받힘 가능 음소로 코딩

            ## 어말의 [ʃ]는 '시'로 적고, 자음 앞의 [ʃ]는 '슈'로, 모음 앞의 [ʃ]는 뒤따르는 모음에 따라 '샤', '섀', '셔', '셰', '쇼', '슈', '시'로 적는다.
            elif (
                phoneme.code == 'ʃ'
                and c.is_next_consonant()
                ):
                output_phoneme_list.append(phoneme)
                output_phoneme_list.append(Phoneme('AP', 'ㅠ', 'vowel'))

            elif phoneme.code == 'ɒ':
                output_phoneme_list.append(Phoneme(phoneme.code, 'ㅗ', phoneme.type))

            else:
                output_phoneme_list.append(phoneme)

        self.phonemes = output_phoneme_list