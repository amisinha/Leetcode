class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        temp = []
        cnt = 0
        for i in range(len(s)):
            temp.append(s[i])
            if i >= 2:
                if len(temp) == len(set(temp)):
                    cnt += 1
                del temp[0]
        return cnt
            
            
            
     
                       
                       
                      
                       
                       
            
        