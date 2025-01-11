
from pieces import Rook, Knight, Bishop, Queen, King, Pawn, get_attacked_pieces, get_piece_by_position

available_pieces = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Pawn']
available_pos_states = ['Empty', 'null']
available_game_states = ['CheckmateWhite', 'CheckmateBlack', 'Stalemate', 'PlayingBlack', 'PlayingBlack', 'KingInCheckWhite', 'KingInCheckBlack']

class BoardFaker:
    def __init__(self):
        self.whitesTook = []
        self.blacksTook = []
        self.gameState = 'PlayingWhite'
        self.turn  = "white"
        self.castlingWhite = True
        self.castlingBlack = True
         
        self.board = [
            [Rook([0, 0], 'black'), Knight([0, 1], 'black'), Bishop([0, 2], 'black'), Queen([0, 3], 'black'), King([0, 4], 'black'), Bishop([0, 5], 'black'), Knight([0, 6], 'black'), Rook([0, 7], 'black')],
            [Pawn([1, 0], 'black'), Pawn([1, 1], 'black'), Pawn([1, 2], 'black'), Pawn([1, 3], 'black'), Pawn([1, 4], 'black'), Pawn([1, 5], 'black'), Pawn([1, 6], 'black'), Pawn([1, 7], 'black')],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            [Pawn([6, 0], 'white'), Pawn([6, 1], 'white'), Pawn([6, 2], 'white'), Pawn([6, 3], 'white'), Pawn([6, 4], 'white'), Pawn([6, 5], 'white'), Pawn([6, 6], 'white'), Pawn([6, 7], 'white')],
            [Rook([7, 0], 'white'), Knight([7, 1], 'white'), Bishop([7, 2], 'white'), Queen([7, 3], 'white'), King([7, 4], 'white'), Bishop([7, 5], 'white'), Knight([7, 6], 'white'), Rook([7, 7], 'white')]
        ]   
        
    def print_board(self):
        for row in self.board:
            for piece in row:
                if piece != 'Empty':
                    print(piece.get_name(), end=' ')
                else:
                    print(piece, end=' ')
            print('\n')
    
    
    def get_piece_by_position(self, position):
        return get_piece_by_position(self.board, position)        
    
    def move_piece(self, origin, destination):
        piece = self.get_piece_by_position(origin)
        if piece == 'Empty':
            return
        if piece.get_color() != self.turn:
            return
        
        if not piece.is_valid_move(destination, self.board):
            return
        
        self.board[destination[0]][destination[1]] = piece
        self.board[origin[0]][origin[1]] = 'Empty'
        piece.position = destination
        self.gameState = 'PlayingBlack' if self.gameState == 'PlayingWhite' else 'PlayingWhite'
            


board_faker = BoardFaker()

board_faker.print_board()

rook = board_faker.get_piece_by_position([0, 0])

print(get_attacked_pieces(board_faker.board, [0, 0], rook.get_kernel(),  rook.get_kernel_type(), rook.get_color()))