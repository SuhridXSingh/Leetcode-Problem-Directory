class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {")":"(","}":"{","]":"["}
        checklist=[]
        for char in s:
            if char=="(" or char=="{" or char=="[":
                checklist.append(char)
            elif char in mapping:
                if checklist:
                    last_opening_bracket = checklist.pop()
                    if last_opening_bracket != mapping[char]:
                        return False
                else:
                    return False
        return not checklist
