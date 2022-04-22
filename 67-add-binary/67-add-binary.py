class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a== "0" and b== "0":
            return "0"
        else:
            
            na = int(a,2)
            nb = int(b,2)
            tot = na+nb
            return bin(tot).lstrip("0b")
        
            
        