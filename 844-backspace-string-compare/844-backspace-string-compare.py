class Solution:
    def compute (self, target):
        res = []
        for i in target:
            if i != '#':
                res.append(i)
            else:
                if res:
                    res.pop()
        return res
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.compute(s) == self.compute(t)
        
 
            
        