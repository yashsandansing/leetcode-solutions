class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # flood fill -> if encounter a 1 -> use dfs to go to all neighbors and set those to 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        def is_valid(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return False
            return True
        def flood_fill(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"
            while q:
                nr, nc = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = nr + dr, nc + dc
                    if is_valid(new_r, new_c):
                        grid[new_r][new_c] = "0"  # ← Mark before enqueue
                        q.append((new_r, new_c))
            return
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    res += 1
                    flood_fill(r, c)

        return res
