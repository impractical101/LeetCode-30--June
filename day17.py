#Submitted by thr3sh0ld
#Logic: start from edges and keep a check of "O" in the edges and rem "O" in the frame to be converted to X. 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row in [0, len(board)-1] or col in [0, len(board[0])-1]) and board[row][col] == 'O':
                    queue.append((row,col))
        while queue:
            row,col = queue.pop(0)
            if 0<=row<len(board) and 0<=col<len(board[0]) and board[row][col] == 'O':
                board[row][col] = 'V'
                queue.append((row-1,col))
                queue.append((row+1,col))
                queue.append((row,col-1))
                queue.append((row,col+1))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'V':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'