class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = []
        f = nums[:n]
        s = nums[n:]
        for i in range(n):
            l.append(f[i])
            l.append(s[i])
        return l
