class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l = []

        for i in range(m):
            l.append(nums1[i])

        new_list = l + nums2

        nums1[:] = new_list
        nums1.sort()
