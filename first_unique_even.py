class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0 and nums.count(nums[i])==1:
                return nums[i]
        return -1
