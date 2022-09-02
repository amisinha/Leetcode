class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        newList = []
        currList =[]
        count =0
        for i in range(lo,hi+1):
            currList.append(i)
            num = i
            while num is not 1:
                count += 1
                if num%2 == 0:
                    num = int(num/2)
                else:
                    num = 3*num +1
            newList.append(count)
            count =0
        pairList = list(zip(newList, currList))
        pairList.sort(key = lambda x:x[0])
        pair = pairList[k-1]
        return pair[1]
        
     
        
        
                
                
        