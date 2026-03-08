class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        l=[]
        for i in range(len(nums)):
            if i+1 not in num_set:
                l.append(i+1)
        return l
