from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        dr = (-1,0,1,0)
        dc = (0,1,0,-1)
        visited = deque()
        answer = 0
        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    visited.append((r,c))
                    continue
                if (r,c) in visited:
                    visited.append((r,c))
                    continue
                queue = deque()
                visited.append((r,c))
                queue.append((r,c))
                local = 1
                while queue:
                    curr_r, curr_c= queue.pop() # DFS
                    for i in range(4):
                        nr = curr_r+dr[i]
                        nc = curr_c+dc[i]
                        if 0 <= nr < m and 0 <= nc < n:
                            if (nr, nc) in visited:
                                continue
                            elif grid[nr][nc]:
                                queue.append((nr, nc))
                                local += 1
                        visited.append((nr,nc))
                answer = max(answer, local)
        return answer
