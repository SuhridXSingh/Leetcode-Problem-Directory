class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        s_to_t = {}
        t_to_s = {}

        for k, v in zip(s, t):
            if k in s_to_t and s_to_t[k] != v:
                return False
            if v in t_to_s and t_to_s[v] != k:
                return False

            s_to_t[k] = v
            t_to_s[v] = k

        return True
