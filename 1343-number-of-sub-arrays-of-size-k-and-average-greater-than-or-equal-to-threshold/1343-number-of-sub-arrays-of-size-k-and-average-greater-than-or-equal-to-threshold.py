class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        tot = 0
        a =0
        
        for i in range(len(arr)):
            tot += arr[i]
            
            if i >= k-1:
                avg = tot/k
                if avg >= threshold:
                    cnt += 1
                tot -= arr[a]
                a += 1
        return cnt
                
            
        