class Solution {
public:
    static const int MOD = 1e9 + 7;

    vector<long long> treeSum, treeSq, lazy;
    int n;

    void apply(int node, int l, int r, long long val) {
        long long len = r - l + 1;

        treeSq[node] = (
            treeSq[node] +
            2LL * val * treeSum[node] +
            val * val % MOD * len
        ) % MOD;

        treeSum[node] = (
            treeSum[node] + val * len
        ) % MOD;

        lazy[node] = (lazy[node] + val) % MOD;
    }

    void push(int node, int l, int r) {
        if (lazy[node] == 0 || l == r)
            return;

        int mid = (l + r) / 2;

        apply(node * 2, l, mid, lazy[node]);
        apply(node * 2 + 1, mid + 1, r, lazy[node]);

        lazy[node] = 0;
    }

    void update(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql)
            return;

        if (ql <= l && r <= qr) {
            apply(node, l, r, 1);
            return;
        }

        push(node, l, r);

        int mid = (l + r) / 2;

        update(node * 2, l, mid, ql, qr);
        update(node * 2 + 1, mid + 1, r, ql, qr);

        treeSum[node] = (
            treeSum[node * 2] + treeSum[node * 2 + 1]
        ) % MOD;

        treeSq[node] = (
            treeSq[node * 2] + treeSq[node * 2 + 1]
        ) % MOD;
    }

    int sumCounts(vector<int>& nums) {
        n = nums.size();

        treeSum.assign(4 * n, 0);
        treeSq.assign(4 * n, 0);
        lazy.assign(4 * n, 0);

        unordered_map<int, int> lastSeen;
        long long answer = 0;

        for (int i = 0; i < n; i++) {
            int x = nums[i];

            int previous = -1;
            if (lastSeen.count(x))
                previous = lastSeen[x];

            update(1, 0, n - 1, previous + 1, i);

            answer = (answer + treeSq[1]) % MOD;

            lastSeen[x] = i;
        }

        return static_cast<int>(answer);
    }
};