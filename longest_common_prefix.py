class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
     
        if not strs:
            return ""
       
        string_1 = strs[0]
        for i in range(len(string_1)):
            for string_2 in strs[1:]:
                if (i>= len(string_2)) or (string_2[i]!=string_1[i]):
                    return  string_1[:i]
        return string_1
