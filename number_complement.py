class Solution:
    def findComplement(self, num: int) -> int:
        b = f"{num:b}"
        s=""

        for i in b:
            s += str(int(i)^1)
        
        i = int(s,2)

        return i
