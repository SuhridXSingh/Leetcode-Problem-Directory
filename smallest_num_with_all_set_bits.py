class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = bin(n)[2:]

        num_bits = len(binary)

        mask = (1 << num_bits) - 1
        bin_mask = bin(mask)[2:]

        comp = n ^ mask

        output = n | comp

        return output
