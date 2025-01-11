

def is_valid_boundary(x, y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

def is_same_position(position1, position2):
    return position1[0] == position2[0] and position1[1] == position2[1]

class Rock:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.kernel = [[0, 1, 0],
                       [1, 0 ,1],
                       [0, 1, 0]]
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
    
    def get_atacking_pieces(self, board):
        x, y = self.position
        pieces = []
        for i in range(0, x):
            if board[i][y] != 'Empty':
                pieces.append(board[i][y])
                break
        for i in range(x + 1, 8):
            if board[i][y] != 'Empty':
                pieces.append(board[i][y])
                break
        for i in range(0, y):
            if board[x][i] != 'Empty':
                pieces.append(board[x][i])
                break
        for i in range(y + 1, 8):
            if board[x][i] != 'Empty':
                pieces.append(board[x][i])
                break
        return pieces            
            

        


class Knight:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.kernel = [[0, 1, 0, 1, 0],
                       [1, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 1],
                       [0, 1, 0, 1, 0]]
        self.kernelType = 'Discrete'
        
class Bishop:
    def __init__(self, position, color):
        self.color = color
        self.position = position
        self.kernel = [[1, 0, 1],
                       [0, 0, 0],
                       [1, 0, 1]]
        self.kernelType = 'Continuous'


class Queen:
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.kernel = [[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]]
        self.kernelType = 'Continuous'

class King:
    def __init__(self, position, color):
        self.color = color
        self.position = position
        self.kernel = [[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]]
        self.kernelType = 'Discrete'
        self.isUnderAttack = False

class Pawn:
    def __init__(self, position, color):
        self.position = position
        self.kernelType = 'Discrete'
        self.isUnderAttack = False
        if color == 'white':
            self.kernel = [[1, 1, 1],
                           [0, 0, 0],
                           [0, 0, 0]]
        else :
            self.kernel = [[0, 0, 0],
                           [0, 0, 0],
                           [1, 1, 1]]    