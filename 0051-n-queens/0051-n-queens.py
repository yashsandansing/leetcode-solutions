class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        board = [["."]*n for _ in range(n)]
        self.result = list()
        self.backtrack(0, board, 0)
        
        return self.result
    def backtrack(self, num_queens: int, curr_board: List[List[str]], curr_row: int) -> None:
        if curr_row > self.n:
            return
        if num_queens == self.n:
            self.result.append(["".join(r) for r in curr_board])
            return
        
        for c in range(self.n):
            if self.can_place(curr_board, curr_row, c):
                curr_board[curr_row][c] = 'Q'
                self.backtrack(num_queens + 1, curr_board, curr_row + 1)
                curr_board[curr_row][c] = '.'
        

    def can_place(self, grid: List[List[str]], row: int, col: int) -> bool:
        
        for r in range(row, -1, -1):
            if grid[r][col] == 'Q':
                return False
        
        r = row
        c = col

        while r >= 0 and c >= 0:
            if grid[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        r = row
        c = col
        while r >= 0 and c <= self.n - 1:
            if grid[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        
        return True