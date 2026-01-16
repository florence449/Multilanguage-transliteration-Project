from word_class.phoneme_context_class import *

class Phoneme:
    """
    음소입니다. ipa, 한글 음소, 음소 유형을 가지고 있습니다.
    """
    __slots__ = ('code', 'kor_code', 'type')

    def __init__(self, code, kor_code, type):
        self.code = code
        self.kor_code = kor_code
        self.type = type

    def __repr__(self):
        return f"Phoneme(code='{self.code}', kor_code='{self.kor_code}', type='{self.type}')"

class Word:
    """
    단어를 표현하는 클레스입니다.
    단어의 음운 변화및 한글식 음절 변화를 구현합니다.
    """

    # 반모음화
    gliding_consonant = {'ʃ', 'ʂ', 'ʝ', 'ɲ', 'tʃ', 'ʒ', 'dʒ'}
    gliding_vowel = {'j', 'jj'}
    gliding_vowel_map = {'ㅏ': 'ㅑ', 'ㅓ': 'ㅕ', 'ㅜ': 'ㅠ', 'ㅗ': 'ㅛ', 'ㅔ': 'ㅖ', 'ㅐ': 'ㅒ', 'ㅣ': 'ㅣ'}

    # 원순모음화
    rounding_vowel = {'w', }
    rounding_vowel_map = {'ㅏ': 'ㅘ', 'ㅓ': 'ㅝ', 'ㅣ': 'ㅟ', 'ㅗ': 'ㅝ', 'ㅜ': 'ㅜ', 'ㅔ': 'ㅞ', 'ㅐ': 'ㅙ'}

    # 자음 결합
    ipa_final_consonant_list = {'l', 'n', 'm', 'ŋ', 'ɐ̃ʊ̃', 'ɐ̃ŋ', 'ɭ', 'ɴ', 'ʎ', 'AP_N'}

    def __init__(self, phonemes):
        self.phonemes = phonemes
        self.syllables = []

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
            elif (not c.is_end_of_word() and  # 인덱스 안정성 확인
                  phoneme.code in self.gliding_consonant and  # 반모음화 조건 확인(반모음화 유발 자음)
                  self.phonemes[i + 1].kor_code in self.gliding_vowel_map):  # 모음의 반모음화 가능성 확인

                output_phoneme_list.append(phoneme)
                output_phoneme_list.append(
                    Phoneme(f'{self.phonemes[i + 1].code}_JC', self.gliding_vowel_map[self.phonemes[i + 1].kor_code],
                            'vowel'))

                skip = True

            elif (not c.is_end_of_word() and  # 인덱스 안정성 확인
                  phoneme.code in self.gliding_vowel and c.is_next_vowel() and  # 반모음화 조건 확인(반모음 j)
                  self.phonemes[i + 1].kor_code in self.gliding_vowel_map):  # 모음의 반모음화 가능성 확인

                output_phoneme_list.append(Phoneme(f'{phoneme.code}{self.phonemes[i + 1].code}_JC',
                                                   self.gliding_vowel_map[self.phonemes[i + 1].kor_code], 'vowel'))

                skip = True

            else:
                output_phoneme_list.append(phoneme)

        self.phonemes = output_phoneme_list

    def rounding(self):
        """
        w가 앞에 있는 모음들의
        원순모음화를 수행합니다.
        """

        output_phoneme_list = []

        skip = False

        for i, phoneme in enumerate(self.phonemes):

            c = PhonemeContext(self.phonemes, i)

            # 앞에서 반모음이 추가되었다면 모음 건너뜀
            if skip:
                skip = False
                pass

            elif (
                    not c.is_end_of_word()
                    and phoneme.code in self.rounding_vowel
                    and c.is_next_vowel()
                    and self.phonemes[i + 1].kor_code in self.rounding_vowel_map):

                output_phoneme_list.append(Phoneme(f'{phoneme.code}{self.phonemes[i + 1].code}_WC',
                                                   self.rounding_vowel_map[self.phonemes[i + 1].kor_code], 'vowel'))

                skip = True

            else:
                output_phoneme_list.append(phoneme)

        self.phonemes = output_phoneme_list

    def nasalization(self):
        """
        비음모음의 끝에 비음을
        추가합니다.
        """

        output_phoneme_list = []

        for i, phoneme in enumerate(self.phonemes):

            c = PhonemeContext(self.phonemes, i)

            if (not c.is_end_of_word() and
                    '̃' in phoneme.code and
                    not self.phonemes[i + 1].code in ('n', 'ŋ', 'm')):

                output_phoneme_list.append(phoneme)
                output_phoneme_list.append(Phoneme('AP_N', 'ㅇ', 'consonant'))

            elif (c.is_end_of_word() and
                  '̃' in phoneme.code):

                output_phoneme_list.append(phoneme)
                output_phoneme_list.append(Phoneme('AP_N', 'ㅇ', 'consonant'))

            elif (not c.is_start_of_word() and
                  phoneme.code in ('n', 'ŋ', 'm') and
                  '̃' in self.phonemes[i - 1].code):

                output_phoneme_list.append(Phoneme(f'{phoneme.code}', 'ㅇ', f'{phoneme.type}'))

            else:
                output_phoneme_list.append(phoneme)

        self.phonemes = output_phoneme_list

    def localization(self):

        """
        지역화 함수입니다. 기본기능은 존재하지 않으며, 영어 등 다른 함수에서 기능을 발휘합니다.
        """

        pass

    def make_syll(self):

        first_in_syll = False
        middle_in_syll = False

        sylls = []
        syll = []

        allowed_onset_after_rounding = {'h', 'k', 'ɡ'}
        can_final_consonant_list = {'m', 'n'}
        only_final_consonant_list = {'ŋ', 'l', 'FC_k', 'FC_p', 'FC_t', 'AP_N'}
        gliding_consonant = {'tʃ', 'ʃ', 'dʒ', 'ʒ'}

        def add_syll_and_reset():
            nonlocal syll, first_in_syll, middle_in_syll
            sylls.append(syll)
            syll = []
            first_in_syll = False
            middle_in_syll = False

        def next_can_final():
            return (
                    c.is_next_consonant()
                    and (
                            (
                                    self.phonemes[i + 1].code in can_final_consonant_list
                                    and (
                                            not c.is_two_next_vowel()
                                            or (
                                                    c.is_two_next_vowel()
                                                    and "WC" in self.phonemes[i + 2].code
                                                    and self.phonemes[i + 1].code not in allowed_onset_after_rounding
                                            )
                                    )
                            )
                            or (self.phonemes[i + 1].code in only_final_consonant_list)
                    )
            )

        for i, phoneme in enumerate(self.phonemes):
            c = PhonemeContext(self.phonemes, i)
            if not syll:  # 음절에 할당된 음소가 없음
                if phoneme.type == 'vowel':  # 현재 음소가 모음
                    syll.extend([Phoneme('AP', 'ㅇ', 'consonant'), phoneme])
                    if next_can_final():
                        middle_in_syll = True  # 중성이 음소에 있음 확인
                    else:  # 다음 음소가 모음이거나 받힘으로 올 수 없는 자음일 경우
                        add_syll_and_reset()  # 음절 초기화

                elif phoneme.type == 'consonant':  # 현재 음소가 자음
                    syll.append(phoneme)
                    if (
                            # 다음 음소가 모음이나 원순 모음이 아닐 것
                            (c.is_next_vowel() and "WC" not in self.phonemes[i + 1].code)
                            # 원순 모음일 경우 원순 모음과 결합을 허용하는 자음일 것
                            or (c.is_next_vowel() and "WC" in self.phonemes[
                        i + 1].code and phoneme.code in allowed_onset_after_rounding)
                    ):
                        first_in_syll = True  # 초성이 음소에 있음 확인

                    elif (
                            c.is_next_consonant()
                            or c.is_end_of_word()
                            or "WC" in self.phonemes[i + 1].code
                    ):
                        if phoneme.code in gliding_consonant:
                            syll.append(Phoneme('AP', 'ㅣ', 'vowel'))
                        else:
                            syll.append(Phoneme('AP', 'ㅡ', 'vowel'))

                        if next_can_final():
                            middle_in_syll = True
                        else:
                            add_syll_and_reset()
                else:  # 현재 음소가 특수문자
                    syll.append(phoneme)
                    add_syll_and_reset()

            elif first_in_syll:  # 초성이 있음
                if next_can_final():
                    syll.append(phoneme)
                    first_in_syll = False
                    middle_in_syll = True
                else:
                    syll.append(phoneme)
                    add_syll_and_reset()

            elif middle_in_syll:  # 중성이 있음
                if c.is_next_vowel() and phoneme.code in ('l',):  # 다음 음소가 모음이고 중성이 될 모음이 있음
                    syll.append(phoneme)
                    add_syll_and_reset()
                    syll.append(phoneme)
                    first_in_syll = True
                else:
                    syll.append(phoneme)
                    add_syll_and_reset()
            else:
                print(f"Error:{phoneme.code} in {''.join(phoneme.code for phoneme in self.phonemes)} is not in syll")

        self.syllables = sylls

    def combine_kor(self):
        # 한글 자음, 모음에 대한 Unicode 값
        choseong = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        jungseong = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                     'ㅣ']
        jongseong = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

        word = ''
        for syllable in self.syllables:
            # 만약 syllable이 한 글자만 있으면, 바로 word에 추가
            if len(syllable) == 1:
                word += syllable[0].kor_code if syllable else ''  # syllable이 비어 있지 않으면 첫 번째 요소 추가

            # 초성, 중성, 종성 결합
            elif len(syllable) >= 2:
                try:
                    cho_index = choseong.index(syllable[0].kor_code)
                    jung_index = jungseong.index(syllable[1].kor_code)

                    # Check if syllable has a jongseong and if it is in the jongseong list
                    jong_index = jongseong.index(syllable[2].kor_code) if len(syllable) == 3 and syllable[
                        2].kor_code in jongseong else 0

                    word += chr(0xAC00 + cho_index * 21 * 28 + jung_index * 28 + jong_index)
                except ValueError as e:
                    # Handle the case where a character is not found in the expected list
                    raise ValueError(f"ValueError processing syllable: {syllable}. Error: {e}")

        return word