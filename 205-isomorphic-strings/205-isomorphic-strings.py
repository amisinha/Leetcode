class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = set(s)
        s2 = set(t)
        
        if len(s1) == len(s2) == len(set(zip(s,t))):
            return True
        return False
       
            
        