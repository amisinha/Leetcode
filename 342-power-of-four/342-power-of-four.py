class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        elif n==1:
            return True
        else:
            newNum = n%4
            if newNum ==0:
                return self.isPowerOfFour(n/4)
            else:
                return False
 
            
                

        