# -----------------------------------------------------------#
# Created by willderose                                      #
# -----------------------------------------------------------#
import math
from . import baseComponent


class ExperienceCurve(baseComponent.BaseComponent):
    """ Will define the way monsters gain experience as they level up
    """

    @classmethod
    def from_yaml(cls, loader, node):
        return cls

    @classmethod
    def getRequiredXpForNextLevel(cls, startingLevel: int) -> int:
        """ Get the experience required for a monster to reach their next level

        :param startingLevel: The level that we're going to be checking for.
        """

        return int(cls.getRequiredXPForLevel(startingLevel + 1) - cls.getRequiredXPForLevel(startingLevel))

    @staticmethod
    def getRequiredXPForLevel(level: int) -> int:
        """ Get the required cumulative experience for the supplied level
        """

        raise NotImplementedError()


class Erratic(ExperienceCurve):
    yaml_tag = '!xpCurve_Erratic'

    @staticmethod
    def getRequiredXPForLevel(level: int) -> int:
        if level < 50:
            totalXpForLevel = ((level ** 3) * (100 - level)) / 50
        elif 50 <= level < 68:
            totalXpForLevel = ((level ** 3) * (150 - level)) / 100
        elif 68 <= level < 98:
            totalXpForLevel = ((level ** 3) * math.floor((1911 - (10 * level)) / 3)) / 500
        else:
            totalXpForLevel = ((level ** 3) * (160 - level)) / 100
        return int(totalXpForLevel)


class Fast(ExperienceCurve):
    yaml_tag = '!xpCurve_Fast'

    @staticmethod
    def getRequiredXPForLevel(level: int) -> int:
        totalXpForLevel = (4 * (level ** 3)) / 5
        return int(totalXpForLevel)


class Fluctuating(ExperienceCurve):
    yaml_tag = '!xpCurve_Fluctuating'

    @staticmethod
    def getRequiredXPForLevel(level: int) -> int:
        if level < 15:
            totalXpForLevel = ((level ** 3) * (math.floor((level + 1) / 3) + 24)) / 50
        elif 15 <= level < 36:
            totalXpForLevel = ((level ** 3) * (level + 14)) / 50
        else:
            totalXpForLevel = ((level ** 3) * (math.floor(level / 2) + 32)) / 50
        return int(totalXpForLevel)


class MediumFast(ExperienceCurve):
    yaml_tag = '!xpCurve_MediumFast'

    @staticmethod
    def getRequiredXPForLevel(level: int) -> int:
        totalXpForLevel = level ** 3
        return int(totalXpForLevel)


class MediumSlow(ExperienceCurve):
    yaml_tag = '!xpCurve_MediumSlow'

    @staticmethod
    def getRequiredXPForLevel(level: int) -> int:
        totalXpForLevel = (6/5) * (level ** 3) - (15 * (level ** 2)) + (100 * level) - 140
        return int(totalXpForLevel)


class Slow(ExperienceCurve):
    yaml_tag = '!xpCurve_Slow'

    @staticmethod
    def getRequiredXPForLevel(level: int) -> int:
        totalXpForLevel = (5 * (level ** 3)) / 4
        return int(totalXpForLevel)
