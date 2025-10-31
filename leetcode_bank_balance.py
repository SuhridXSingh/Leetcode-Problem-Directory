class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        days = n%7


        if weeks<1:
            amt = (days/2)*(2+(days-1))
        elif weeks == 1:
            amt = 28 + (days/2)*(2*(weeks+1)+(days-1))
        elif weeks>1:
            amt = (days/2)*(2*(weeks+1)+(days-1)) + (weeks/2)*(56+(weeks-1)*7)
        else:
            amt = 0   
        return int(amt)
