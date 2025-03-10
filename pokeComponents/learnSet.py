# -----------------------------------------------------------#
# Created by willderose                             #
# -----------------------------------------------------------#
from dataclasses import dataclass
from typing import Type
from . import move
from . import baseComponent


@dataclass
class LearnSet(baseComponent.BaseComponent):
    """ A learn set defines which moves a monster can learn through various means
    """

    yaml_tag = '!learnSet'

    # Defines which monsters will impart which moves on a monster's children
    BY_BREEDING: tuple[tuple, Type[move.Move]]

    # Defines which moves a monster learns by acquiring levels
    BY_LEVEL_UP: dict[int: list[Type[move.Move], ]]

    # Defines which moves a monster can learn through technical machines
    BY_TECHNICAL_MACHINE: list[Type[move.Move]] = ()

    # Defines which moves can be learned by a monster via move tutors
    BY_TUTOR: list[Type[move.Move]] = ()

    @classmethod
    def from_yaml(cls, loader, node):
        return LearnSet(**loader.construct_mapping(node))

    def __post_init__(self):
        self._moveNames = None

    @property
    def moveNames(self) -> list[Type[move.Move], ]:
        """ Get a flattened list of moves that the pokeMonster can learn for easier iteration
        """

        if self._moveNames is not None:
            return self._moveNames

        moveList = list(self.BY_TUTOR + self.BY_TECHNICAL_MACHINE)
        for _, moveClasses in self.BY_LEVEL_UP.items():
            moveList.extend(moveClasses)

        self._moveNames = (moveClass.NAME for moveClass in moveList)

        return self._moveNames

    def getMovesForLevel(self, level: int) -> list[Type[move.Move], ]:
        """ Get the list of moves that a monster has by default for the supplied level number

        :param level: Which level we're going to define as a breakpoint
        """

        movesForLevel = []
        for levelNo, moveClasses in self.BY_LEVEL_UP.items():
            if levelNo > level:
                break

            movesForLevel.extend(moveClasses)

        return movesForLevel

    def moveIsValid(self, moveInstance: move.Move) -> bool:
        """ Validate the supplied move instance against the moves defined in this learn set to figure out whether the
        move can be learned by this learn set's attached monster
        """

        return moveInstance.NAME in self.moveNames