# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def inbound(r, c):
            return -1 < r < ROWS and -1 < c < COLS

        q = deque([(0,0,0)])
        v = set([(0,0)])

        while q:
            o, r, c = q.popleft()

            if (r, c) == (ROWS-1, COLS-1):
                return o
            
            for nr, nc in [(r-1, c),(r+1, c),(r, c-1),(r, c+1)]:
                if not inbound(nr, nc):
                    continue
                if (nr, nc) in v:
                    continue

                if grid[nr][nc]:
                    q.append((o + 1, nr, nc))
                else:
                    q.appendleft((o, nr, nc))

                v.add((nr, nc))