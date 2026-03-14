class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        l = [1] * n
        rp = 1
        max_possible_sum = 10**15
        for i in range(n - 1, -1, -1):

            l[i] = rp
            rp *= nums[i]
            if rp > max_possible_sum:
                rp = max_possible_sum
            
        ls = 0
        for i in range(n):

            if ls == l[i]:
                return i

            ls += nums[i]

        return -1
