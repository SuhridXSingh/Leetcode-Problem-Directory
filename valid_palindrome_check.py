class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        for char in s:
            if char.isalnum():
                clean_string += char
        clean_string = clean_string.lower()
        if clean_string == clean_string[::-1]:
            return True
        else:
            return False
