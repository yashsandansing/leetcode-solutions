class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        ROWS = len(board)
        COLS = len(board[0])
        def bfs(row: int, col: int) -> None:
            visit = set()
            q = deque()
            q.append((row, col))
            visit.add((row, col))
            while q:
                r, c = q.popleft()
                mines = neighboring_mines(r, c)
                
                if mines != 0:
                    board[r][c] = str(mines)
                    
                if mines == 0:
                    board[r][c] = "B"
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and board[nr][nc] == "E":
                            q.append((nr, nc))
                            visit.add((nr, nc))

        
        def neighboring_mines(row: int, col: int) -> int:
            mines = 0
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if board[nr][nc] == "M":
                        mines += 1
                
            return mines

        if board[row][col] == "E":
            bfs(row, col)
        
        return board