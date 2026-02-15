class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        ROWS = len(board)
        COLS = len(board[0])

        def check(r, c):
            # base case -> check for oob or if ele = '.'
            if r<0 or r>=ROWS or c < 0 or c >= COLS or board[r][c] == ".":
                return False
            return True
        
        ships = 0

        for r in range(ROWS):
            for c in range(COLS):
                # increment X by 1 with each encounter
                if board[r][c] == "X":
                    ships += 1
                    # since no two ships can be adjacent
                    # check if this ships is the continuation
                    # of a ship by checking left or right
                    # if left or right returns True, decrement num_ships by 1
                    # else we just encountered a new ship
                    if check(r-1, c) or check(r, c-1):
                        ships -= 1
        
        return ships