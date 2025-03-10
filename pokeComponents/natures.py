# -----------------------------------------------------------#
# Created by willderose                              #
# -----------------------------------------------------------#
import random
from dataclasses import dataclass
from typing import Type
from . import pokeStats
from . import baseComponent


class _BaseNature(baseComponent.BaseComponent):
    """ A monster's nature defines which stat has an advantage and which is at a disadvantage when used by a monster in battle
    """

    @classmethod
    def from_yaml(cls, loader, node):
        return cls

    FAVORED_STAT: Type[pokeStats.PokeStat] = None
    FAVORED_FLAVOUR = None  # TODO

    NON_FAVORED_STAT: Type[pokeStats.PokeStat] = None
    NON_FAVOURED_FLAVOR = None  # TODO


class Adamant(_BaseNature):
    yaml_tag = '!nature_Adamant'
    FAVORED_STAT = pokeStats.Attack
    NON_FAVORED_STAT = pokeStats.SpecialAttack


class Bashful(_BaseNature):
    yaml_tag = '!nature_Bashful'


class Bold(_BaseNature):
    yaml_tag = '!nature_Bold'
    FAVORED_STAT = pokeStats.Defense
    NON_FAVORED_STAT = pokeStats.Attack


class Brave(_BaseNature):
    yaml_tag = '!nature_Brave'
    FAVORED_STAT = pokeStats.Attack
    NON_FAVORED_STAT = pokeStats.Speed


class Calm(_BaseNature):
    yaml_tag = '!nature_Calm'
    FAVORED_STAT = pokeStats.SpecialDefense
    NON_FAVORED_STAT = pokeStats.Attack


class Careful(_BaseNature):
    yaml_tag = '!nature_Careful'
    FAVORED_STAT = pokeStats.SpecialDefense
    NON_FAVORED_STAT = pokeStats.SpecialAttack


class Docile(_BaseNature):
    yaml_tag = '!nature_Docile'


class Gentle(_BaseNature):
    yaml_tag = '!nature_Gentle'
    FAVORED_STAT = pokeStats.SpecialDefense
    NON_FAVORED_STAT = pokeStats.Defense


class Hardy(_BaseNature):
    yaml_tag = '!nature_Hardy'


class Hasty(_BaseNature):
    yaml_tag = '!nature_Hasty'
    FAVORED_STAT = pokeStats.Speed
    NON_FAVORED_STAT = pokeStats.Defense


class Impish(_BaseNature):
    yaml_tag = '!nature_Impish'
    FAVORED_STAT = pokeStats.Defense
    NON_FAVORED_STAT = pokeStats.SpecialAttack


class Jolly(_BaseNature):
    yaml_tag = '!nature_Jolly'
    FAVORED_STAT = pokeStats.Speed
    NON_FAVORED_STAT = pokeStats.SpecialAttack


class Lax(_BaseNature):
    yaml_tag = '!nature_Lax'
    FAVORED_STAT = pokeStats.Defense
    NON_FAVORED_STAT = pokeStats.SpecialDefense


class Lonely(_BaseNature):
    yaml_tag = '!nature_Lonely'
    FAVORED_STAT = pokeStats.Attack
    NON_FAVORED_STAT = pokeStats.Defense


class Mild(_BaseNature):
    yaml_tag = '!nature_Mild'
    FAVORED_STAT = pokeStats.SpecialAttack
    NON_FAVORED_STAT = pokeStats.Defense


class Modest(_BaseNature):
    yaml_tag = '!nature_Modest'
    FAVORED_STAT = pokeStats.SpecialAttack
    NON_FAVORED_STAT = pokeStats.Attack


class Naive(_BaseNature):
    yaml_tag = '!nature_Naive'
    FAVORED_STAT = pokeStats.Speed
    NON_FAVORED_STAT = pokeStats.SpecialDefense


class Naughty(_BaseNature):
    yaml_tag = '!nature_Naughty'
    FAVORED_STAT = pokeStats.Attack
    NON_FAVORED_STAT = pokeStats.SpecialDefense


class Quiet(_BaseNature):
    yaml_tag = '!nature_Quiet'
    FAVORED_STAT = pokeStats.SpecialAttack
    NON_FAVORED_STAT = pokeStats.Speed


class Quirky(_BaseNature):
    yaml_tag = '!nature_Quirky'


class Rash(_BaseNature):
    yaml_tag = '!nature_Rash'
    FAVORED_STAT = pokeStats.SpecialAttack
    NON_FAVORED_STAT = pokeStats.SpecialDefense


class Relaxed(_BaseNature):
    yaml_tag = '!nature_Relaxed'
    FAVORED_STAT = pokeStats.Defense
    NON_FAVORED_STAT = pokeStats.Speed


class Sassy(_BaseNature):
    yaml_tag = '!nature_Sassy'
    FAVORED_STAT = pokeStats.SpecialDefense
    NON_FAVORED_STAT = pokeStats.Speed


class Serious(_BaseNature):
    yaml_tag = '!nature_Serious'


class Timid(_BaseNature):
    yaml_tag = '!nature_Timid'
    FAVORED_STAT = pokeStats.Speed
    NON_FAVORED_STAT = pokeStats.Attack


def _getRandomNature() -> Type[_BaseNature]:
    """ Get a random nature out of the ones defined in this file
    """

    natures = [Adamant,
               Bashful,
               Bold,
               Brave,
               Calm,
               Careful,
               Docile,
               Gentle,
               Hardy,
               Hasty,
               Impish,
               Jolly,
               Lax,
               Lonely,
               Mild,
               Modest,
               Naive,
               Naughty,
               Quiet,
               Quirky,
               Rash,
               Relaxed,
               Sassy,
               Serious,
               Timid]

    return natures[random.randrange(len(natures))]