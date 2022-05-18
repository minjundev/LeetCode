from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        dr = (-1,0,1,0)
        dc = (0,1,0,-1)
        queue = deque()
        visited = deque()
        queue.append((sr, sc))
        visited.append((sr, sc))
        candidates = [(sr, sc)]
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if 0 <= nr < m and 0 <= nc < n:
                    if (nr, nc) in visited:
                        continue
                    elif image[nr][nc] == image[sr][sc]:
                        candidates.append((nr, nc))
                        queue.append((nr, nc))
                        visited.append((nr, nc))
        for r, c in candidates:
            image[r][c] = newColor
        return image
