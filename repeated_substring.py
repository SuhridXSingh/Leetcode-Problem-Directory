class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # n = len(s)
        # for i in range(1, (n // 2) + 1):
        #     if n % i == 0:
        #         sub = s[:i]
        #         if sub * (n // i) == s:
        #             return True
        # return False

        # big_s = s*2
        # big_s = big_s[1:-1]
        # if s in big_s:
        #     return True
        # else:
        #     return False

        return s in (s * 2)[1:-1]
