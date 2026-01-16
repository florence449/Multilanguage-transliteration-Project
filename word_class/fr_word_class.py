from word_class.main_class import *
from word_class.phoneme_context_class import *

class FrWord(Word):
    """
    프랑스어 음운변화를 반영하는 메스드의 집합입니다.
    """

    gliding_consonant = {'ʃ', 'ʂ', 'ʝ', 'ɲ', 'tʃ', 'dʒ'}

    def gliding(self):
        """
        j가 앞에 있는 모음들의
        반모음화를 수행합니다.
        """

        output_phoneme_list = []

        skip = False

        for i, phoneme in enumerate(self.phonemes):

            c = PhonemeContext(self.phonemes, i)

            # 앞에서 반모음이 추가되었다면 모음 건너뜀
            if skip:
                skip = False
                pass

            # 반모음화 유발 자음에서 반모음화 진행
            elif (not c.is_end_of_word() and # 인덱스 안정성 확인
                  phoneme.code in self.gliding_consonant and # 반모음화 조건 확인(반모음화 유발 자음)
                  self.phonemes[i+1].kor_code in self.gliding_vowel_map): # 모음의 반모음화 가능성 확인

                output_phoneme_list.append(phoneme)
                output_phoneme_list.append(Phoneme(f'{self.phonemes[i+1].code}_JC', self.gliding_vowel_map[self.phonemes[i+1].kor_code], 'vowel'))

                skip = True

            elif (not c.is_end_of_word() and # 인덱스 안정성 확인
                  phoneme.code in self.gliding_vowel and
                  c.is_next_vowel() and
                  c.is_prev_vowel() and
                  self.phonemes[i+1].kor_code in self.gliding_vowel_map): # 모음의 반모음화 가능성 확인

                output_phoneme_list.append(Phoneme(f'{phoneme.code}{self.phonemes[i+1].code}_JC', self.gliding_vowel_map[self.phonemes[i+1].kor_code], 'vowel'))

                skip = True

            else:
                output_phoneme_list.append(phoneme)

        self.phonemes = output_phoneme_list

    def rounding(self):
        """
        w가 앞에 있는 모음들의
        원순모음화를 수행합니다.
        """

        pass

    def localization(self):

        final_phoneme_dict = {
            'ㅍ':'ㅂ', 'ㅋ':'ㄱ', 'ㅌ':'ㅅ'
        }

        output_phoneme_list = []

        for i, phoneme in enumerate(self.phonemes):

            c = PhonemeContext(self.phonemes, i)

            if c.is_end_of_word() and phoneme.code in self.gliding_vowel:
                output_phoneme_list.append(Phoneme(phoneme.code, 'ㅠ', phoneme.type))

            # 프랑스어 모음 변형
            elif not c.is_start_of_word() and phoneme.code in ('ə', 'w') and self.phonemes[i-1].code in ('ɲ', 'ʃ'):
                output_phoneme_list.append(Phoneme(phoneme.code, 'ㅠ', phoneme.type))

            elif phoneme.code == 'ə':
                output_phoneme_list.append(Phoneme(phoneme.code, 'ㅡ', phoneme.type))

            elif (
                phoneme.code in ('p', 't', 'k') # 무성 파열음
                and c.is_prev_vowel() and not '̃' in self.phonemes[i-1].code # 이전 모음이 구강모음
                and c.is_next_consonant() and self.phonemes[i+1].code in ('p', 't', 'k', 'f', 's', 'ʃ', 'h') # 이후 자음이 파열음 혹은 마찰음
            ):
                output_phoneme_list.append(Phoneme(f"FC_{phoneme.code}", final_phoneme_dict[phoneme.kor_code], phoneme.type))

            elif (c.is_end_of_word() or not c.is_next_vowel()) and phoneme.code in ('ʃ', 'ɲ'):
                output_phoneme_list.append(phoneme)
                output_phoneme_list.append(Phoneme('AP', 'ㅠ', 'vowel'))

            elif (c.is_end_of_word() or not c.is_next_vowel()) and phoneme.code == 'ʒ':
                output_phoneme_list.append(phoneme)
                output_phoneme_list.append(Phoneme('AP', 'ㅜ', 'vowel'))

            else:
                output_phoneme_list.append(phoneme)

        self.phonemes = output_phoneme_list