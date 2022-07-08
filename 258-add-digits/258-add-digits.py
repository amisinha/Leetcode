class Solution:
    def addDigits(self, num: int) -> int:
        t = 0
        while num !=0:
            r = num%10
            t += r
            num = int(num/10)
        if t>9:
            return self.addDigits(t)
        else:
            return t
 
        
            
            
     
            
       
            
            
          
        
 

                    

    

       
        
            
        
                
    
            
        
        