class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex = rowIndex+1
        if rowIndex == 1:
            return [1]
        elif rowIndex == 2:
            return [1,1]
        else:
            res = [[1],[1,1]]
            for i in range(2,rowIndex):
                row =[1]
                for j in range(1,i):
                    num = res[i-1][j-1] + res[i-1][j]
                    row.append(num)
                row.append(1)
                res.append(row)
            return res[rowIndex-1]
        