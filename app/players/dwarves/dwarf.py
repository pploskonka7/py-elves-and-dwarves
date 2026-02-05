
from app.players.player import Player

class Dwarf(Player):
    def __init__(self, favourite_dish):
        self.favourite_dish = favourite_dish

    @abstractmethod
    def eat_favourite_dish(self):
        print(f"{nickname} is eating {self.favourite_dish}")
