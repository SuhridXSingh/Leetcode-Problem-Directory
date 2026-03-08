class Solution:
    def minOperations(self, s: str) -> int:
        c0 = 0
        for i in range(len(s)):
            if i%2==0 and s[i]!="0":
                c0+=1
            if i%2!=0 and s[i]!="1":
                c0+=1
        c1 = len(s)-c0
        return min(c0,c1)
