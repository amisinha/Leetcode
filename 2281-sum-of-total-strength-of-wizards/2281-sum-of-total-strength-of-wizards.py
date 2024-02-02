class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod = 10**9 + 7
        A = [0] + strength + [0] 
        P = list(itertools.accumulate(itertools.accumulate(A), initial=0))
        
        stack = [0] 
        result = 0
        
        for right in range(len(A)):
            while A[stack[-1]] > A[right]:
                left, i = stack[-2], stack.pop()
                pos = (i - left) * (P[right] - P[i])
                neg = (right - i) * (P[i] - P[left])
                result += A[i] * (pos - neg)
            stack.append(right)
            
        return result % mod
 