
from app.players.elves.elf import Elf

class ElfRanger(Elf):
    def __init__(self, _bow_level: int):
        self.bow_level = _bow_level