class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        x_inverse = x_str[::-1]

        if "-" in x_inverse:
            x_inverse = x_inverse.replace("-", "")
            x_inverse = "-" + x_inverse

        reversed_num = int(x_inverse)

        if reversed_num < -(2**31) or reversed_num > 2**31 - 1:
            return 0

        return reversed_num
