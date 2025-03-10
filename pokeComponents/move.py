# -----------------------------------------------------------#
# Created by willderose                              #
# -----------------------------------------------------------#
from dataclasses import dataclass
from typing import Type
from . import pokeTypes
from . import moveEffects
from . import baseComponent


@dataclass
class Move(baseComponent.BaseComponent):
    """ A move is what monsters can do inside and outside of battle.
    """

    yaml_tag = '!pokeMove'

    ACCURACY: int
    CATEGORY: None  # TODO
    DESCRIPTION: str
    EFFECTS: list[Type[moveEffects.MoveEffect], ]
    MOVE_TYPE: Type[pokeTypes.PokeType]
    NAME: str
    POWER: int
    POWER_POINTS: int

    FROM_HIDDEN_MACHINE: bool = False
    PRIORITY: int = 0

    def __post_init__(self):
        self._currentPowerPoints = self.POWER_POINTS

    @classmethod
    def from_yaml(cls, loader, node):
        return Move(**loader.construct_mapping(node))

    def loadFromSavedYaml(self, *args, **kwargs):
        self._currentPowerPoints = kwargs.get('CURRENT_POWER_POINTS')
