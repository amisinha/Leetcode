class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string= ''.join(char for char in s if char.isalnum() ).lower()
        reverseString = new_string[::-1]
        if reverseString == new_string:
            return True
        else:
            return False
        
        