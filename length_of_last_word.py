class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_of_words = s.split()
        # list_of_words.remove("")
        last_word = list_of_words.pop()
        return len(last_word)
