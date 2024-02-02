class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        possibleDigits = "123456789"
        
        for startDigit in possibleDigits:
            num = int(startDigit)
            curr_num = int(startDigit)
            
            while num <= high and curr_num < 9:
                curr_num += 1
                num = num*10 + curr_num
                
                if num >= low and num <= high:
                    result.append(num)
        return sorted(result)
            
            
        
        
        