class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                ransomNote = ransomNote.replace(i,"",1)
                magazine = magazine.replace(i,"",1)
                
                
                
        if(len(ransomNote) ==0):
            return True
        else:
            return False
        