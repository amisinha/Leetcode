class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        for r in range(numRows):
            increment = (numRows-1)*2
            for i in range(r, len(s), increment):
                result = result+s[i]
                
                if(r>0 and r< numRows-1 and i+increment - 2*r < len(s)):
                    result = result+s[i+increment - 2*r]
        return result
                    
        