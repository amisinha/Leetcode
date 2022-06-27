class Solution:
    def longestPalindrome(self, s: str) -> int:
        flag = False
        values = Counter(s).values()
        c =0
        
        for v in values:
            if v%2 == 0:
                c += v
            else:
                flag = True
                c += (v//2)*2
        if flag:
            c += 1
        return c
                
            
        
        