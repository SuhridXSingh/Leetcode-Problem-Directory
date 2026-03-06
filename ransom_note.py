class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag = list(magazine)

        for i in ransomNote:
            if i in mag:
                mag.remove(i)
            else:
                return False
        
        return True

        
