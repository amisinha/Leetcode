class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x:x[1], reverse= True)
        tot = 0
        remainingBoxes = truckSize
        for i in boxTypes:
            boxes = min(remainingBoxes, i[0])
            tot += boxes* i[1]
            remainingBoxes -= boxes
        return tot
        