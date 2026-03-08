class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l = []
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry > 0:
            if p1 >= 0:
                d1 = int(num1[p1])
            else:
                d1 = 0
            if p2 >= 0:
                d2 = int(num2[p2])
            else:
                d2 = 0
            t = d1 + d2 + carry
            carry = t // 10
            l.append(str(t % 10))
            p1 -= 1
            p2 -= 1
        l = l[::-1]
        r = "".join(l)
        return r
