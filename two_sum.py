class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices= []
        for i in range(len(nums)):
            for a in range(i+1,len(nums)):
                if nums[i]+ nums[a] == target:
                    indices.append(i)
                    indices.append(a)
        return indices
