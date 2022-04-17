class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        new =[]
        i=0
        total = 0
        k=1
        for i in range(l):
            total = total + digits[i]*pow(10,(l-k)) 
            k=k+1 
        nTot = total+1
        result = list(map(int, str(nTot)))
        return result
            
    
            
            
        
       
        
        
            
            
        