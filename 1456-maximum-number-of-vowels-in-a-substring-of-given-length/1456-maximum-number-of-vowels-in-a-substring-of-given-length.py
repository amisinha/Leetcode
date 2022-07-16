class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxE = float('-inf')
        temp = []
        vowels = ['a','e','i','o','u']
        cnt = 0
        
        for i in range(len(s)):
            if s[i] in vowels:
                cnt+= 1
            temp.append(s[i])
            if i>= k-1:
                maxE = max(maxE, cnt)
                if temp[0] in vowels:
                    cnt -= 1
                del temp[0]
        return maxE
            
            
  
           
            
        
        