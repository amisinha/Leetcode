class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        elif n==1:
            return True
        else:
            newNum = n%3
            if newNum == 0:
                return self.isPowerOfThree(n/3)
            else:
                return False
        
  
            
            
        