class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        def get_valid_neighbors(r, c):
            directions = [(r, c+1), (r, c-1), (r+1, c), (r-1, c), \
            (r+1, c+1), (r+1, c-1), (r-1, c-1), (r-1, c+1)]
            neighbors = []
            for dr, dc in directions:
                if not 0 <= dr < n or not 0 <= dc < n: 
                    continue
                if grid[dr][dc] != 0:
                    continue
                # print('here')
                neighbors.append((dr, dc))

            return neighbors

        q = deque()
        q.append((0, 0))
        grid[0][0] = 1

        while q:
            r, c = q.popleft()
            if (r, c) == (n - 1, n - 1):
                return grid[n - 1][n - 1]
            valid_neighbors = get_valid_neighbors(r, c)
            for nr, nc in valid_neighbors:
                grid[nr][nc] = 1 + grid[r][c]
                q.append((nr, nc))

        return -1