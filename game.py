from enum import Enum

class Game:
    
    def __init__(self, size):
        self.x = 0
        self.y = 0
        self.board = Board(size)
        self.hunger = 0

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y

    def get_known_board(self):
        return self.board
    
    def edit_board(self, x, y, o:GameObject):
        self.board.edit_board(x, y, o)

    def more_hunger(self):
        self.hunger += 1
    
    def get_hunger(self):
        return self.hunger

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[GameObject.EMPTY for _ in range(size)] for _ in range(size)]
    
    def get_board(self):
        return self.board
    
    def edit_board(self, x, y, o:GameObject):
        self.board[x][y] = o

    def get_at_position(self, x, y)->GameObject:
        return self.board[x][y]

class GameObject(Enum):
    EMPTY = 0
    WALL = 1
    FOOD = 2
    PLAYER = 3