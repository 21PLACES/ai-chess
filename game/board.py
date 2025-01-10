

available_pieces = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Pawn']

class BoardFaker:
    def __init__(self):
        self.board = [
            ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook'],
            ['Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn'],
            ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook']
        ]
        
        
    def is_valid_move_rock(self, initial_pos, target_pos):
        # Get the piece at the initial position
        piece = self.board[initial_pos[0]][initial_pos[1]]
        
        # Check if the piece is a Rook
        if piece != 'Rook':
            return False
        
        # Get the row and column of the target position
        target_row, target_col = target_pos
        
        # Get the row and column of the initial position
        initial_row, initial_col = initial_pos
        
        # Check if the target position is within the board boundaries
        if target_row < 0 or target_row >= len(self.board) or target_col < 0 or target_col >= len(self.board[0]):
            return False
        
        # Check if the target position is in the same row or column as the initial position
        if target_row != initial_row and target_col != initial_col:
            return False
        
        # Check if there are any pieces between the initial and target positions
        if target_row == initial_row:
            # Check if there are any pieces between the initial and target columns
            start_col = min(initial_col, target_col)
            end_col = max(initial_col, target_col)
            for col in range(start_col + 1, end_col):
                if self.board[initial_row][col] != 'Empty':
                    return False
        else:
            # Check if there are any pieces between the initial and target rows
            start_row = min(initial_row, target_row)
            end_row = max(initial_row, target_row)
            for row in range(start_row + 1, end_row):
                if self.board[row][initial_col] != 'Empty':
                    return False
        
        return True

    def is_valid_move_knight(self, initial_pos, target_pos):
        # Get the piece at the initial position
        piece = self.board[initial_pos[0]][initial_pos[1]]
        
        # Check if the piece is a Knight
        if piece != 'Knight':
            return False
        
        # Get the row and column of the target position
        target_row, target_col = target_pos
        
        # Get the row and column of the initial position
        initial_row, initial_col = initial_pos
        
        # Check if the target position is within the board boundaries
        if target_row < 0 or target_row >= len(self.board) or target_col < 0 or target_col >= len(self.board[0]):
            return False
        
        # Calculate the absolute difference in rows and columns
        row_diff = abs(target_row - initial_row)
        col_diff = abs(target_col - initial_col)
        
        # Check if the move is a valid knight move
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            return True
        
        return False
    
    def print_board(self):
        for row in self.board:
            print(row)

# Create an instance of the BoardFaker class
board_faker = BoardFaker()

# Print the chess board
board_faker.print_board()