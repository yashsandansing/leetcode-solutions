class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def add_to_set(r, c, label):
            q = deque([])
            visit = set()
            q.append((r, c))
            visit.add((r, c))
            area = 0
            while q:
                nr, nc = q.popleft()
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = label
                    area += 1
                    for dr, dc in [[nr + 1, nc], [nr - 1, nc], [nr, nc + 1], [nr, nc - 1]]:
                        if (dr, dc) not in visit:
                            q.append((dr, dc))
                            visit.add((dr, dc))
            return area
        
        def curr_max(r, c, n):
            visit = set()
            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            total_area = 1
            for dr, dc in directions:
                if 0 <= dr < n and 0 <= dc < n and grid[dr][dc] not in visit:
                    visit.add(grid[dr][dc])
                    total_area += id_to_area[grid[dr][dc]]

            return total_area

        n = len(grid)
        
        id_to_area = defaultdict(int)
        label = 2

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    id_to_area[label] = add_to_set(r, c, label)
                    label += 1
        
        max_area = 0 if len(id_to_area) == 0 else max(id_to_area.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    max_area = max(max_area, curr_max(r, c, n))

        return max_area