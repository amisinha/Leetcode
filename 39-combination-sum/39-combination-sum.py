class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def findAll(target,i,elements,res):
            if i == len(candidates):
                if target == 0:
                    return res.append(elements.copy())
                return
            elif target == 0:
                res.append(elements.copy())
                return
            elif target <0:
                return
            else:
                findAll(target-candidates[i],i,elements+[candidates[i]],res)
                findAll(target,i+1,elements,res)
        findAll(target,0,[],res)
        return res
        