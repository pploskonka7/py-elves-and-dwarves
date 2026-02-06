
from abc import ABC

from app.players.elves.elf import Elf


class Druid(Elf, ABC):
    def __init__(
            self,
            nickname: str,
            play_elf_song: str,
            _favourite_spell: str
    ) -> None:
        super().__init__(nickname, play_elf_song)
        self._favourite_spell = _favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return (f""
                f"Druid {self.nickname}. "
                f"{self.nickname} has a favourite spell: "
                f"{self._favourite_spell}")
