class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        temp =[]
        for ind, i in enumerate(number):
            if  i == digit:
                temp.append(int(number[:ind] + number[ind+1:]))
        return str(max(temp))
        