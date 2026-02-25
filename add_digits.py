class Solution:
    def addDigits(self, num: int) -> int:

        s = str(num)

        if len(s) == 1:
            return num

        while len(s) > 1:
            n = 0
            for i in range(len(s)):
                n += int(s[i])

            s = str(n)

        return int(s)
