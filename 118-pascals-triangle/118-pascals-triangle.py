class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            res = [[1],[1,1]]
        for i in range(2,numRows):
            row =[1]
            for j in range(1,i):
                num = res[i-1][j-1] + res[i-1][j]
                row.append(num)
            row.append(1)
            res.append(row)
        return res
        
        