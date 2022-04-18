class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        newList = []
        i=0
        c=1
        j=1
        for i in range(len(score)):
            for j in range(len(score)):
                if score[i]< score[j]:
                    c=c+1
                    j=j+1
            newList.append(str(c))
            c=1
            i=i+1
        for j in range(len(newList)):
            if newList[j]== "1":
                newList[j] = "Gold Medal"
            elif newList[j] == "2":
                newList[j] = "Silver Medal"
            elif newList[j] == "3":
                newList[j] = "Bronze Medal"
            else:
                j=j+1
                
        return newList
                
           
            
            
        