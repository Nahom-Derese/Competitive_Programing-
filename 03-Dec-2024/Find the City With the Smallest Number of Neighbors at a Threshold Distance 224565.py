# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def floyd_warshall(self, n, edges):
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i, j, w in edges:
            dist[i][j] = dist[j][i] = w
        
        for i in range(n):
            dist[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        return dist
        
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        distances = self.floyd_warshall(n, edges)
        counts = []

        for i in range(n):
            count = 0
            for j in range(n):
                count += distances[i][j] <= distanceThreshold
            counts.append(count)

        ans = 0
        min_count = float("inf")
        for i, num in enumerate(counts):
            if num <= min_count:
                ans = i
                min_count = num
        
        return ans