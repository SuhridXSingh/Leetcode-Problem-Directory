class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()

        if len(pattern) != len(l):
            return False

        letter_to_word = {}
        word_to_letter = {}

        for k, v in zip(pattern, l):

            if k in letter_to_word and letter_to_word[k] != v:
                return False

            if v in word_to_letter and word_to_letter[v] != k:
                return False

            letter_to_word[k] = v
            word_to_letter[v] = k

        return True
