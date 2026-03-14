class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        c = 0
        for i in range(len(s)):
            c += abs(i - t.find(s[i]))
        return c
