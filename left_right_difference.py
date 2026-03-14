class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        left_sum = 0
        right_sum = sum(nums)
        for i in nums:
            right_sum -= i
            ans.append(abs(right_sum - left_sum))
            left_sum += i
        return ans
