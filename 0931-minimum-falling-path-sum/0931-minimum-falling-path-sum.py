class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(1, rows):
            for c in range(cols):
                matrix[r][c] = matrix[r][c] + min (matrix[r-1][max(0,c-1)], matrix[r-1][c],
                                                   matrix[r-1][min(cols-1,c+1)])
        return min(matrix[-1])
        
        
        
        