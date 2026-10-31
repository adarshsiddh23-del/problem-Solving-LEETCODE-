class Solution {
public:
    const int MOD = 1e9 + 7;
    int m, n;

    vector<vector<vector<int>>> memo;

    int solve(int i, int j, int dir, vector<vector<int>>& grid) {
        if (i >= m || j >= n)
            return -1;

        if (memo[i][j][dir] != -2)
            return memo[i][j][dir];

        // Empty cell: valid destination
        if (grid[i][j] == 0)
            return memo[i][j][dir] = i * n + j;

        // Mirror: reflect and change direction
        if (dir == 0) {
            // Entered from left (moving right)
            // Reflect down
            return memo[i][j][dir] =
                solve(i + 1, j, 1, grid);
        } 
        else {
            // Entered from above (moving down)
            // Reflect right
            return memo[i][j][dir] =
                solve(i, j + 1, 0, grid);
        }
    }

    int uniquePaths(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();

        memo.assign(m, vector<vector<int>>(
            n, vector<int>(2, -2)
        ));

        vector<vector<long long>> dp(
            m, vector<long long>(n, 0)
        );

        dp[0][0] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (dp[i][j] == 0)
                    continue;

                if (i == m - 1 && j == n - 1)
                    continue;

                // Move right
                if (j + 1 < n) {
                    int pos = solve(i, j + 1, 0, grid);

                    if (pos != -1) {
                        int x = pos / n;
                        int y = pos % n;

                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD;
                    }
                }

                // Move down
                if (i + 1 < m) {
                    int pos = solve(i + 1, j, 1, grid);

                    if (pos != -1) {
                        int x = pos / n;
                        int y = pos % n;

                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD;
                    }
                }
            }
        }

        return dp[m - 1][n - 1];
    }
};