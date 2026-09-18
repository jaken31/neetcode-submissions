class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            seen_r = set()
            for num in row:
                if num != ".":
                    if num in seen_r:
                        return False
                    seen_r.add(num)
                else:
                    continue

        for i in range(len(board[0])):
            seen_c = set()
            for j in range(len(board)):
                num = board[j][i]
                if num != ".":
                    if num in seen_c:
                        return False
                    seen_c.add(num)
                else:
                    continue
        
        for subgrid in range(9):
            seen_s = set()
            start_row = (subgrid // 3) * 3
            start_col = (subgrid % 3) * 3
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    num = board[row][col]
                    if num != ".":
                        if num in seen_s:
                            return False
                        seen_s.add(num)
                    else:
                        continue
        return True
                    