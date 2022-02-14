class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        val=0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l= l+1
            charSet.add(s[r])
            val = max(val,r-l+1)
        return val
                
            
        