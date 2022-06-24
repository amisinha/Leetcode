class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if len(s)> len(t):
            return False
        else:
            for i in t:
                if j<len(s) and s[j] == i:
                    j += 1
            return len(s) == j
        