class Solution:
    def scoreOfString(self, s: str) -> int:
        a = 0
        for i in range(len(s)-1):
            a += abs(ord(s[i])-ord(s[i+1]))
        return a
