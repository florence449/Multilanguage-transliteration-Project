class PhonemeContext:
    """
    주어진 음소 리스트 내 특정 위치의 주변 환경을
    판별하는 기능을 제공하는 클래스.
    """

    def __init__(self, word, i):
        self.word = word
        self.i = i
        self.length = len(word)

    def is_prev_consonant(self):
        """이전 음소가 자음인지 확인"""
        return self.i > 0 and self.word[self.i - 1].type == 'consonant'

    def is_next_consonant(self):
        """다음 음소가 자음인지 확인"""
        return self.i + 1 < self.length and self.word[self.i + 1].type == 'consonant'

    def is_prev_vowel(self):
        """이전 음소가 모음인지 확인"""
        return self.i > 0 and self.word[self.i - 1].type == 'vowel'

    def is_next_vowel(self):
        """다음 음소가 모음인지 확인"""
        return self.i + 1 < self.length and self.word[self.i + 1].type == 'vowel'

    def is_prev_syllabic(self):
        """이전 음소가 음절성인지 확인"""
        return self.i > 0 and self.word[self.i - 1].type == 'syllabic'

    def is_next_syllabic(self):
        """다음 음소가 음절성인지 확인"""
        return self.i + 1 < self.length and self.word[self.i + 1].type == 'syllabic'

    def is_two_prev_consonant(self):
        """2개 이전 음소가 자음인지 확인"""
        return self.i > 1 and self.word[self.i - 2].type == 'consonant'

    def is_two_next_consonant(self):
        """2개 다음 음소가 자음인지 확인"""
        return self.i + 2 < self.length and self.word[self.i + 2].type == 'consonant'

    def is_two_prev_vowel(self):
        """2개 이전 음소가 모음인지 확인"""
        return self.i > 1 and self.word[self.i - 2].type == 'vowel'

    def is_two_next_vowel(self):
        """2개 다음 음소가 모음인지 확인"""
        return self.i + 2 < self.length and self.word[self.i + 2].type == 'vowel'

    def is_two_prev_syllabic(self):
        """2개 이전 음소가 음절성인지 확인"""
        return self.i > 1 and self.word[self.i - 2].type == 'syllabic'

    def is_two_next_syllabic(self):
        """2개 다음 음소가 음절성인지 확인"""
        return self.i + 2 < self.length and self.word[self.i + 2].type == 'syllabic'

    def is_end_of_word(self):
        """특수 문자를 고려하여 단어의 끝인지 확인"""
        return (
            self.i + 1 == self.length or
            (self.i + 1 < self.length and self.word[self.i + 1].type in {'special', 'syllabic'})
        )

    def is_start_of_word(self):
        """특수 문자를 고려하여 단어의 시작인지 확인"""
        return (
            self.i == 0 or
            (self.i > 0 and self.word[self.i - 1].type in {'special', 'syllabic'})
        )
