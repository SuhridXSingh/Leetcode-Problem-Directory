class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x^y
        b = f"{n:b}"
        return b.count("1")
