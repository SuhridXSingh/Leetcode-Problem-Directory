class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_string = "".join(map(str,digits))
        num_int = int(num_string)
        new_num = num_int + 1
        new_num_str = str(new_num)
        new_list = [int(char) for char in new_num_str]
        return new_list
