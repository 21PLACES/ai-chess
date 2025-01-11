
from game.pieces import Rock, Knight, Bishop, Queen, King, Pawn

available_pieces = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Pawn']
available_pos_states = ['Empty', 'null']
available_game_states = ['CheckmateWhite', 'CheckmateBlack', 'Stalemate', 'PlayingBlack', 'PlayingBlack', 'Kingnull']

class BoardFaker:
    def __init__(self):
        self.whitesTook = []
        self.blacksTook = []
        self.gameState = 'PlayingWhite'
        self.board = [
            [Rock([0, 0], 'black'), Knight([0, 1], 'black'), Bishop([0, 2], 'black'), Queen([0, 3], 'black'), King([0, 4], 'black'), Bishop([0, 5], 'black'), Knight([0, 6], 'black'), Rock([0, 7], 'black')],
            [Pawn([1, 0], 'black'), Pawn([1, 1], 'black'), Pawn([1, 2], 'black'), Pawn([1, 3], 'black'), Pawn([1, 4], 'black'), Pawn([1, 5], 'black'), Pawn([1, 6], 'black'), Pawn([1, 7], 'black')],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
            [Pawn([6, 0], 'white'), Pawn([6, 1], 'white'), Pawn([6, 2], 'white'), Pawn([6, 3], 'white'), Pawn([6, 4], 'white'), Pawn([6, 5], 'white'), Pawn([6, 6], 'white'), Pawn([6, 7], 'white')],
            [Rock([7, 0], 'white'), Knight([7, 1], 'white'), Bishop([7, 2], 'white'), Queen([7, 3], 'white'), King([7, 4], 'white'), Bishop([7, 5], 'white'), Knight([7, 6], 'white'), Rock([7, 7], 'white')]
        ]
        
        
    def print_board(self):
        for row in self.board:
            print(row)


board_faker = BoardFaker()


board_faker.print_board()