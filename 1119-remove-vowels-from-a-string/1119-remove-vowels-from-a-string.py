class Solution:
    def removeVowels(self, s: str) -> str:
        newString = ""
        for i in s:
            if i not in 'aeiou':
                newString += i
        return newString
        