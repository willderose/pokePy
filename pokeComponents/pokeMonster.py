# -----------------------------------------------------------#
# Created by willderose                              #
# -----------------------------------------------------------#
from dataclasses import dataclass
from typing import Type

from importlib import reload
from . import baseComponent
from . import eggGroups
from . import experienceCurves
from . import learnSet
from . import move
from . import natures
from . import pokeStats
from . import pokeTypes


@dataclass
class PokeMonster(baseComponent.BaseComponent):
    """ A monster is the main attraction for this whole system. It has:
        - stats that affect its battle performance
        - moves that can be used in battle
        - a variety of metadata used for its classification in the bestiary
    """

    yaml_tag = '!pokeMonster'

    NAME: str

    POKEMON_TYPES: list[Type[pokeTypes.PokeType], ]

    # Stats
    HEALTH_POINTS: Type[pokeStats.PokeStat]
    ATTACK: Type[pokeStats.PokeStat]
    DEFENSE: Type[pokeStats.PokeStat]
    SPECIAL: Type[pokeStats.PokeStat]  # Will be used with a gen 1 ruleset
    SPECIAL_ATTACK: Type[pokeStats.PokeStat]
    SPECIAL_DEFENSE: Type[pokeStats.PokeStat]
    SPEED: Type[pokeStats.PokeStat]
    FRIENDSHIP: Type[pokeStats.PokeStat]

    # Classification data
    NUMBER: int
    DESCRIPTION: str
    CATEGORY: None  # TODO
    COLOR: str
    SHAPE: None  # TODO
    FOOTPRINT: None  # TODO
    HEIGHT: int
    WEIGHT: float

    # Egg data
    EGG_GROUP: Type[eggGroups.EggGroup]
    HATCH_TIME: int

    # Learn set
    LEARN_SET: Type[learnSet.LearnSet]

    # Miscellaneous battle data
    EXPERIENCE_CURVE: Type[experienceCurves.ExperienceCurve]
    XP_YIELD: int
    EV_YIELD: dict

    @classmethod
    def from_yaml(cls, loader, node):
        return PokeMonster(**loader.construct_mapping(node))

    def __post_init__(self):
        """ Initialise the private attributes we'll use when necessary
        """

        self.stats = {self.HEALTH_POINTS.name(): self.HEALTH_POINTS,
                      self.ATTACK.name(): self.ATTACK,
                      self.DEFENSE.name(): self.DEFENSE,
                      self.SPECIAL.name(): self.SPECIAL,
                      self.SPECIAL_ATTACK.name(): self.SPECIAL_ATTACK,
                      self.SPECIAL_DEFENSE.name(): self.SPECIAL_DEFENSE,
                      self.SPEED.name(): self.SPEED}

        self._level = 1
        self._moves = None
        self._nature = None
        self._nickname = None

    @property
    def level(self) -> int:
        """ Get this monster's level
        """

        return self._level

    @level.setter
    def level(self, newLevel: int):
        """ Reset all the necessary stat calculations when level changes
        """

        for _, pokeStat in self.stats.items():
            pokeStat.level = newLevel

        self._level = newLevel

    @property
    def moves(self):
        """ When querying this when there are no pre-set moves, get the 4 latest moves according to the Pokemon's level
        """

        if self._moves is not None:
            return self._moves

        self._moves = self.LEARN_SET.getMovesForLevel(self.level)[-4:]

        return self._moves

    @moves.setter
    def moves(self, newMoves: list[Type[move.Move]]):
        """ Before setting the supplies move list, validate the desired moves against this Pokemon's learn set
        """

        for moveInstance in newMoves:
            if not self.LEARN_SET.moveIsValid(moveInstance):
                raise RuntimeError('Move {} cannot be learned by {}'.format(moveInstance.NAME, self.NAME_EN))

        self._moves = newMoves

    @property
    def nature(self) -> Type[natures._BaseNature]:
        """ Get this monster's nature or generate a random one if none are already assigned
        """

        if self._nature is not None:
            return self._nature

        self.nature = natures._getRandomNature()
        return self._nature

    @nature.setter
    def nature(self, newNature: Type[natures._BaseNature]):
        """ Sets the multipliers on this pokeMonster's stats to reflect the nature's favorable and non favorable ones
        """

        if newNature.FAVORED_STAT:
            self.stats[newNature.FAVORED_STAT.name()].natureMultiplier = pokeStats.PokeStat.FAVORABLE_NATURE_BONUS

        if newNature.NON_FAVORED_STAT:
            self.stats[newNature.NON_FAVORED_STAT.name()].natureMultiplier = pokeStats.PokeStat.NON_FAVORABLE_NATURE_BONUS

        self._nature = newNature

    def loadFromSavedYaml(self, **kwargs):
        """ When loading a saved pokeMonster that differs from any defaults, apply those values here
        """

        self.level = kwargs.get('LEVEL', self._level)
        self.nature = kwargs.get('NATURE', self._nature)

        for statName, innateValue in kwargs.get('INNATE_VALUES', {}).items():
            self.stats[statName].innateValue = innateValue

        for statName, effortValue in kwargs.get('EFFORT_VALUES', {}).items():
            self.stats[statName].effortValues = effortValue

        self.moves = kwargs.get('MOVES', self.moves)

