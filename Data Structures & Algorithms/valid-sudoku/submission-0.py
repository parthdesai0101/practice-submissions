from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) #key will be (r/3, c/3)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".": #need to skip over
                    continue
                # check if entry is in our visited row and col sets
                if (board[row][col] in rows[row] or board[row][col] in cols[col]):
                    return False
                if (board[row][col] in squares[(row // 3, col // 3)]):
                    return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        return True
                