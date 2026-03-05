class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        L = []
        i = 0

        while i < len(nums):
            l = []
            strt = i
            end = i
            l.append(nums[strt])
            while end + 1 < len(nums) and nums[end + 1] - nums[end] == 1:
                end += 1

            if strt != end:
                l.append(nums[end])

            if len(l) == 1:
                L.append(str(l[0]))
            else:
                L.append(f"{l[0]}->{l[1]}")

            i = end + 1

        return L
