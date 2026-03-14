class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        all_set = set(allowed)
        c = 0
        for i in range(len(words)):
            is_consistent = True
            for j in range(len(words[i])):
                if words[i][j] not in all_set:
                    is_consistent = False
                    break
            if is_consistent:
                c+=1
        return c
