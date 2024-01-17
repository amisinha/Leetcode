class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        newList = Counter(arr)
        valueList = set(newList.values())
        return len(newList) == len(valueList)