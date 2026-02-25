class Solution:
    def reverseBits(self, n: int) -> int:

        binary = f"{n:032b}"

        bin_string = str(binary)

        rev_string = bin_string[::-1]

        rev_int = int(rev_string, 2)

        return rev_int
