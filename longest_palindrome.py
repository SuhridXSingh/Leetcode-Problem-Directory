class Solution:
    def longestPalindrome(self, s: str) -> int:

        bucket = set()
        length = 0

        for i in s:
            if i in bucket:
                bucket.remove(i)
                length += 2
            else:
                bucket.add(i)

        if len(bucket)!=0:
            length += 1
        
        return length
