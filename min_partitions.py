class Solution:
    def minPartitions(self, n: str) -> int:
        l = [int(x) for x in n]
        return max(l)
