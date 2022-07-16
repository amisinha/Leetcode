class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        cnt = 0
        newS = ""
        for i in range(len(s)):
            newS += s[i]
            if i >= k-1:
                newI = int(newS)
                if newI != 0:
                    if num % newI == 0:
                        cnt += 1
                newS = newS[1:]
        return cnt
            
                
            
        