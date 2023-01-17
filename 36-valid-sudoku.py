class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and not self.is_valid(i, j, board):
                    return False
        
        return True
    
    def is_valid(self, i, j, b):
        return (
            self.is_valid_in_row(i, j, b) and 
            self.is_valid_in_col(i, j, b) and 
            self.is_valid_in_block(i, j, b)
        )
    
    def is_valid_in_row(self, i, j, b):
        for k in range(9):
            if j != k and b[i][j] == b[i][k]:
                return False

        return True


    def is_valid_in_col(self, i, j, b):
        for k in range(9):
            if i != k and b[i][j] == b[k][j]:
                return False

        return True

    def is_valid_in_block(self, i, j, b):
        block_row = int(i / 3) * 3
        block_col = int(j / 3) * 3
        for r in range(block_row, block_row + 3):
            for c in range(block_col, block_col + 3):
                if (r != i or c != j) and b[i][j] == b[r][c]:
                    return False
    
        return True
        
         
