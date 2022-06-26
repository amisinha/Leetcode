class Solution:
    def secondHighest(self, s: str) -> int:
        myset = set()
        temp =[]
        for i in s:
            if i.isdigit():
                myset.add(int(i))
        for i in myset:
            temp.append(i)
        temp.sort()
        if len(temp) == 0 or len(temp) ==1:
            return -1
        else:
            return temp[len(temp)-2]
        
    
        