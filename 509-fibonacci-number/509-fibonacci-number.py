class Solution:
    def fib(self, n: int) -> int:
        assert n>=0 and int(n) == n, "Unsupported input"
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        