class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        l=[]
        for i in nums:
            if i in seen:
                l.append(i)
            else:
                seen.add(i)
        return l
