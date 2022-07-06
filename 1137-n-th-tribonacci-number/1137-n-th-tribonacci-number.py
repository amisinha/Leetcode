class Solution:
    def tribonacci(self, n: int) -> int:
        newList = [0,1,1]
        if n <3:
            return newList[n]
        else:
            for i in range(3,n+1):
                newList.append(newList[i-1]+ newList[i-2]+ newList[i-3])
        return newList[n]
      
            
        