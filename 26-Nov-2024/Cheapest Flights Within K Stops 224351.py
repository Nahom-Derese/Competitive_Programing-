# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float("inf")] * n
        prev[src] = 0

        for i in range(min(n-1, k+1)):
            current = prev[:]

            relaxations = 0
            for u, v, w in flights:
                if current[v] > prev[u] + w:
                    current[v] = prev[u] + w
                    relaxations += 1
            
            if not relaxations:
                return -1 if prev[dst] == float("inf") else prev[dst]

            prev = current[:]
        
        return -1 if prev[dst] == float("inf") else prev[dst]