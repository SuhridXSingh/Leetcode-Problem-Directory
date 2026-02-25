class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        l = [1]
        lf = [1,1]

        if rowIndex == 0:
            return l

        if rowIndex == 1:
            return lf

        if rowIndex>1 :
            for i in range(rowIndex-1):
                l = lf.copy()
                lf.clear()
                lf.append(1)

                for j in range(len(l)-1):
                    lf.append(l[j]+l[j+1])
            
                lf.append(1)
            
            return lf
