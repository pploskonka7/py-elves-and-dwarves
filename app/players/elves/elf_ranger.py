from abc import ABC

from app.players.elves.elf import Elf


class ElfRanger(Elf, ABC):
    def __init__(
            self,
            nickname: str,
            play_elf_song: str,
            _bow_level: int
    ) -> None:
        super().__init__(nickname, play_elf_song)
        self._bow_level = _bow_level

    def get_rating(self) -> int:
        return 3 * self._bow_level

    def player_info(self) -> str:
        return (f""
                f"Elf ranger {self.nickname}. "
                f"{self.nickname} has bow of the "
                f"{self._bow_level} level")
