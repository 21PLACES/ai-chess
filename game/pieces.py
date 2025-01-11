def kernel_convolution(kernel, board, x, y):
    result = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if is_valid_boundary(x + i, y + j):
                result += kernel[i + 1][j + 1] * board[x + i][y + j]
    return result

def get_piece_by_position(board, position):
    x, y = position
    return board[x][y]

def validate_move_by_kernel(kernel,kernelType, board, x, y):
    if kernelType == 'Continuous':
        for i in range(0, 3):
            for j in range(0, 3):
                if kernel[i][j] == 1 and board[x + i - 1][y + j - 1] != 'Empty':
                    return False
    else:
        for i in range(0, 5):
            for j in range(0, 5):
                if kernel[i][j] == 1 and board[x + i - 2][y + j - 2] != 'Empty':
                    return False
    return True
    

def get_attacked_pieces(board, position, kernel, kernel_type, color):
    """
    Determines the pieces under attack based on the kernel of a chess piece.

    Args:
        board (list[list]): 2D list representing the chessboard.
        position (tuple): (row, col) of the piece's position.
        kernel (list or list[tuple]): The kernel defining the attack pattern.
        kernel_type (str): "Continuous" or "Discrete".

    Returns:
        list[tuple]: Positions of the pieces under attack.
    """
    rows, cols = len(board), len(board[0])
    attacked = []

    row, col = position

    if kernel_type == "Discrete":
        for dr, dc in kernel:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and board[r][c] is not None and board[r][c].color != color:
                attacked.append((r, c))

    elif kernel_type == "Continuous":
        for dr, dc in kernel:
            r, c = row + dr, col + dc
            while 0 <= r < rows and 0 <= c < cols:
                if board[r][c] != "Empty":
                    if board[r][c].color != color:
                        attacked.append((r, c))
                    break
                r += dr
                c += dc

    return attacked



def is_valid_boundary(x, y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

def is_same_position(position1, position2):
    return position1[0] == position2[0] and position1[1] == position2[1]

class Rook:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.kernel = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.kernelType = 'Continuous' 
        
    def is_valid_move(self, new_position, board):
        x1, y1 = self.position
        x2, y2 = new_position

        if not is_valid_boundary(x2, y2):
            return False

        if is_same_position(self.position, new_position):
            return False

        if x1 != x2 and y1 != y2:
            return False

        if x1 == x2:
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                if board[x1][y] != "Empty":
                    return False
        else:
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                if board[x][y1] != "Empty":
                    return False
                
        if board[x2][y2] == "Empty" or board[x2][y2].color != self.color:
            return True
        return False
    
    def move(self, new_position, board):
        if not self.is_valid_move(new_position, board):
            return False
        x1, y1 = self.position
        x2, y2 = new_position
        board[x1][y1] = 'Empty'
        self.position = new_position
        board[x2][y2] = self
        return True    
    def get_kernel(self):
        return self.kernel
    def get_kernel_type(self):
        return self.kernelType
    def get_position(self):
        return self.position
    def get_color(self):
        return self.color
    def get_atacking_pieces(self, board):
        return get_attacked_pieces(board, self.position, self.kernel, self.kernelType)           
    def get_name(self):
        return self.color+ ' Rook'
    

        


class Knight:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.kernel = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        self.kernelType = 'Discrete'
    def get_kernel(self):
        return self.kernel
    def get_kernel_type(self):
        return self.kernelType
    def get_position(self):
        return self.position
    def get_color(self):
        return self.color
    def get_atacking_pieces(self, board):
        return get_attacked_pieces(board, self.position, self.kernel, self.kernelType)    
    def get_name(self):
        return self.color + ' Knight'

class Bishop:
    def __init__(self, position, color):
        self.color = color
        self.position = position
        self.kernel = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.kernelType = 'Continuous'
    def get_kernel(self):
        return self.kernel
    def get_kernel_type(self):
        return self.kernelType
    def get_position(self):
        return self.position
    def get_color(self):
        return self.color
    def get_atacking_pieces(self, board):
        return get_attacked_pieces(board, self.position, self.kernel, self.kernelType)    
    def get_name(self):
        return self.color + ' Bishop'

class Queen:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.kernel = [
                    (-1, 0), (1, 0), (0, -1), (0, 1),  
                    (-1, -1), (-1, 1), (1, -1), (1, 1)
                ]  
        self.kernelType = 'Continuous'
    def get_name(self):
        return self.color + ' Queen'

class King:
    def __init__(self, position, color):
        self.color = color
        self.position = position
        self.kernel = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]
        self.kernelType = 'Discrete'
        self.isUnderAttack = False
    def get_name(self):
        return self.color + ' King'

class Pawn:
    def __init__(self, position, color):
        self.position = position
        self.kernelType = 'Discrete'
        self.isUnderAttack = False
        self.color = color
        if color == 'white':
            self.kernel = [(-1, -1), (-1, 1)]
        else :
            self.kernel = [(1, -1), (1, 1)]
    
    def get_name(self):
        return self.color + ' Pawn'    