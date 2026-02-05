
from app.players.elves.elf import Elf

class Druid(Elf):
    def __init__(self, _favourite_spell: str):
        self.favourite_spell = _favourite_spell