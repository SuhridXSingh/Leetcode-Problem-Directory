class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        l = []
        e = 0
        for i in nums:
            if i % 2 == 0:
                e += 1
        o = len(nums) - e
        for i in range(e):
            l.append(0)
        for i in range(o):
            l.append(1)
        return l
