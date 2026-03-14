class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = set()
        for i in s:
            if i not in seen:
                seen.add(i)
        return len(seen)
