class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        index = -1
        c = float('inf')
        for i in range(len(capacity)):
            t=0
            if capacity[i]>=itemSize:
                t = capacity[i]-itemSize
                if t<c:
                    c = t
                    index = i   
        return index
