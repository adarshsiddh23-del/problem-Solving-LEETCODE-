import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:

        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')

        dist = [[INF] * (k + 1) for _ in range(n)]

        pq = []

        dist[0][1] = 0
        heapq.heappush(pq, (0, 0, 1))

        while pq:

            cost, u, cnt = heapq.heappop(pq)

            if cost != dist[u][cnt]:
                continue

            if u == n - 1:
                return cost

            for v, w in adj[u]:

                if labels[u] == labels[v]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_cnt]:

                    dist[v][new_cnt] = new_cost

                    heapq.heappush(
                        pq, (new_cost, v, new_cnt)
                    )

        return -1