class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        newList= [0,1,2]
        
        for i in range(3,n+1):
            newList.append(newList[i-1]+newList[i-2])
        return newList[n]
      
        
        