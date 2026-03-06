class Solution:
    def convertToBase7(self, num: int) -> str:
        l = []

        if num == 0:
            return "0"

        n = abs(num)
        while n > 0:
            l.append(str(n % 7))
            n //= 7

        s = "".join(l)

        f = s[::-1]

        if num < 0:
            return f"-{f}"

        return f
