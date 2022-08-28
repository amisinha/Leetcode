class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ""
        const = ""
        newString = ""
        c1= 0
        c2 = 0
        for i in s:
            if i in 'aeiouAEIOU':
                vowels += i
            else:
                const += i
        vowels = vowels[::-1]
        for i in s:
            if i not in 'aeiouAEIOU':
                newString += const[c1]
                c1 += 1
            else:
                newString += vowels[c2]
                c2 += 1
        return newString
                
            
        
        