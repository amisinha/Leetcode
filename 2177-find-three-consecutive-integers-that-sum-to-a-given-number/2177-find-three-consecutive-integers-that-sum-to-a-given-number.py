class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        newList =[]
        if num%3 != 0:
            return []
        else:
            midNum = int(num/3)
            newList.append(midNum-1)
            newList.append(midNum)
            newList.append(midNum+1)
        return newList
            
        