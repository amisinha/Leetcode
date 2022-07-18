class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        elements = list(range(1,n+1))
        res = []
        
        def findAll(i,ans):
            if len(ans) == k:
                res.append(ans[:])
                return
            for j in elements[i:]:
                ans.append(j)
                findAll(i+1,ans)
                ans.pop()
                i+=1
        findAll(0,[])
        return res
        
        