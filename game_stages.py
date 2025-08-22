from enum import Enum, auto


class GameStages(Enum):
    """Represent the different stages of the game lifecycle."""

    START = auto()
    PAUSE = auto()
    IN_GAME = auto()
