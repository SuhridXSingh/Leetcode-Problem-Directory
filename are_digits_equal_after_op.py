class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            next_s_list = []
            for i in range(len(s) - 1):
                next_s_list.append(str((int(s[i]) + int(s[i + 1])) % 10))
            s = "".join(next_s_list)
        return s[0] == s[1]
