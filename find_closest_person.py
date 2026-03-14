class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        while x!=z and y!=z:
            if y>z:
                y-=1
            else:
                y+=1
            if x>z:
                x-=1
            else:
                x+=1
        if x==z and y==z:
            return 0
        elif x==z:
            return 1
        elif y==z:
            return 2
