class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        sub1 = s[:k]
        sub2 = s[k:]
        sub1 = sub1[::-1]
        return sub1+sub2
