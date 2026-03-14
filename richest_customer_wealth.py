class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wf = 0
        for i in range(len(accounts)):
            wt = 0
            for j in range(len(accounts[i])):
                wt += accounts[i][j]
            if wt>wf:
                wf = wt
        return wf
