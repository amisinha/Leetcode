class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        leftb = [ '(', '{', '[']
        rightb = [ ')', '}', ']']
        
        for i in s:
            if i in leftb:
                st.append(i)
            elif i in rightb:
                if len(st) is not 0 and st[-1] == leftb[rightb.index(i)]:
                    st.pop()
                else:
                    return False
        return len(st) == 0
  
       
      
                        
                    
                    
            
        