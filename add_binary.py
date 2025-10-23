class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        dec_val_1 = int(a,2)
        dec_val_2 = int(b,2)
        x = dec_val_1 + dec_val_2
        return (bin(x))[2:]
