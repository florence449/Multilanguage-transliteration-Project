from translater.lag_code.common_code import *


class SpenishCode(CommonCode):
    """
    스페인어 음운변화를 반영하는 메서드의 집합입니다.
    """
    gliding_vowel = set()

    def localization(self):

        final_phoneme_dict = {
            'ㅋ':'ㄱ', 'ㅍ':'ㅂ'
        }

        output_phoneme_list = []

        for i, phoneme in enumerate(self.phonemes):

            c = PhonemeContext(self.phonemes, i)
            if (
                c.is_next_consonant() and phoneme.code in ('k', 'p') and self.phonemes[i + 1].code == 's'
                ):
                output_phoneme_list.append(Phoneme(f"FC_{phoneme.code}", final_phoneme_dict[phoneme.kor_code], phoneme.type))

            else:
                output_phoneme_list.append(phoneme)

        self.phonemes = output_phoneme_list