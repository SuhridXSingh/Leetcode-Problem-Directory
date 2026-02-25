class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            binary = f"{i:b}"
            ans.append(binary.count("1"))

        return ans
