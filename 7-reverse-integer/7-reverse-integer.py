class Solution:
    def reverse(self, x: int) -> int:
            if x>0:
                
                s =0
                while x != 0:
                    
                    r = x%10
                    s = s*10 + r
                    x = floor(x/10)
                if s in range(pow(-2,31), pow(2,31)):
                    return s
                else:
                    return 0
                
            else:
                
                s =0
                nn = -x
                while nn != 0:
                    
                    r = nn%10
                    s = s*10 + r
                    nn = floor(nn/10)
                if s in range(pow(-2,31), pow(2,31)):
                    
                    return -s
                else:
                    return 0
                
      
            
        
            
        