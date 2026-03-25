class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = []
        n = len(boxes)
        for i in range(n):
            c = 0
            for j in range(n):
                if boxes[j] == "1":
                    c+= abs(i-j)
            l.append(c)
        return l
