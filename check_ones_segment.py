class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = s.count("1")
        sl = s[:n]
        if "0" in sl:
            return False
        return True
