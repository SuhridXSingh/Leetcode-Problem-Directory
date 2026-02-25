class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        binary = f"{n:b}"

        s = str(binary)

        for a in s:
            if a == "1":
                count += 1
            else:
                continue

        return count
