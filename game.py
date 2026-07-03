from enum import Enum
import yaml

class GameObject(Enum):
    EMPTY = 0
    WALL = 1
    FOOD = 2
    PLAYER = 3

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

class Game:
    
    def __init__(self, size):

        # Load training weights from config.yml
        with open("config.yml", "r") as f:
            config = yaml.safe_load(f)
            self.hunger_weight = config.get("hunger_weight", 1.0)
            self.kills_weight = config.get("kills_weight", 2.0)
            self.lifetime_weight = config.get("lifetime_weight", 0.5)

        self.x = 0
        self.y = 0
        self.board = Board(size)
        self.saturation = 100
        self.kills = 0
        self.lifetime = 0

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
        if self.saturation > 0:
            self.saturation -= 1
        else:
            self.saturation = 0
    
    def get_hunger(self):
        return self.saturation

    def get_training_score(self):
        score = (
            (self.kills * self.kills_weight) +
            (self.lifetime * self.lifetime_weight) +
            (self.saturation * self.hunger_weight)
        )
        return score

    def get_score(self):
        score = self.kills + self.lifetime + self.saturation
        return score
