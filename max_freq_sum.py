class Solution:
    def maxFreqSum(self, s: str) -> int:
        v=["a","i","o","u","e"]
        vc = 0
        cc = 0
        for i in s:
            if i in v:
                if s.count(i)>vc:
                    vc = s.count(i)
            else:
                if s.count(i)>cc:
                    cc = s.count(i)
        return vc+cc
