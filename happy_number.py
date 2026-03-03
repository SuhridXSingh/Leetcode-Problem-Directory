class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        seen = set()

        while n != 1:
            new_num = 0
            for i in range(len(s)):
                new_num += int(s[i]) ** 2

            n = new_num
            s = str(new_num)

            if n in seen:
                return False
            else:
                seen.add(n)

        if n == 1:
            return True
