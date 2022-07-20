class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = (a&b)<<1
        xor = a^b
        return res+xor
        