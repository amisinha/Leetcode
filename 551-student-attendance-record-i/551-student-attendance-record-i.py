class Solution:
    def checkRecord(self, s: str) -> bool:
        aCount = 0
        for i in s:
            if i == 'A':
                aCount += 1
        if aCount >1:
            return False
        for i in range(len(s)-2):
            if s[i] == 'L' and s[i+1] == 'L' and s[i+2]== 'L':
                return False
        return True
            
        
        
        