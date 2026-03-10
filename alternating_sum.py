class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        e = sum(nums[x] for x in range(len(nums)) if x%2==0)
        o = sum(nums[x] for x in range(len(nums)) if x%2!=0)
        return e-o
