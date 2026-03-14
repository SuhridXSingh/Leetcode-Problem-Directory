class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        for i in range(len(command)):
            if command[i] == "G":
                s += "G"

            if command[i] == "(" and command[i + 1] == ")":
                s += "o"

            if command[i] == "(" and command[i + 1] == "a":
                s += "al"
        return s
