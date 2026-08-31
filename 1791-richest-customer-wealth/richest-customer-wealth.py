class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0

        for i in range(len(accounts)):
            wealth = 0

            for j in range(len(accounts[i])):
                wealth += accounts[i][j]

            if wealth > ans:
                ans = wealth

        return ans