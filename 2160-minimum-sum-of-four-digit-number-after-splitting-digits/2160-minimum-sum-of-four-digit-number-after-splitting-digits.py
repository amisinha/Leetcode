class Solution:
    def minimumSum(self, num: int) -> int:
        newList = []
        while num is not 0:
            newList.append(num%10)
            num = int(num/10)
        newList.sort()
        num1 = newList[0]*10 + newList[2]
        num2 = newList[1]*10 + newList[3]
        
        return num1+ num2