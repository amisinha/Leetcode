
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        elif n == 1:
            return True
        else:
            newNum = n%2
            if newNum == 0:
                return self.isPowerOfTwo(n/2)
            else:
                return False
        
        
        
        