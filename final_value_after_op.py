class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0
        for operation in operations:
            if operation == "X++" or operation == "++X":
                X += 1
            elif operation == "X--" or operation == "--X":
                X -= 1
        return X
