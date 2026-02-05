
from app.players.player import Player

class Elf(Player):
    def __init__(self, _musical_instrument):
        self._musical_instrument = _musical_instrument

    @abstractmethod
    def play_elf_song(self):
        print(f"{nickname} is playing a song on the {self._musical_instrument}")
