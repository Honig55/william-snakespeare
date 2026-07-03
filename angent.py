from game import Game, Gameobject, Board

class Agent:

    @abstractmethod
    def get_name(self):
        return "William-Shakespeare"

    def get_color(self):
        return '#4EABD1' # shakespeare blue

    def get_author(self):
        return None

    @abstractmethod
    def start(self, game: Game):
        pass

    @abstractmethod
    def move(self, game: Game) -> MoveAction:
        pass

    @abstractmethod
    def end(self, game: Game):
        pass
