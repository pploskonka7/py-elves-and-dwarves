
from app.players.dwarves.dwarf import Dwarf

class DwarfBlacksmith(Dwarf):
    def __init__(self, _skill_level: int):
        self.skill_level = _skill_level
