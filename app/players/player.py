
from abc import ABC, abstractmethod


class Player(ABC):
    pass

@abstractmethod
def get_rating():
    pass

@abstractmethod
def player_info():
    pass