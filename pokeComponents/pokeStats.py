# -----------------------------------------------------------#
# Created by willderose                             #
# -----------------------------------------------------------#

import random

from importlib import reload

from . import baseComponent


class PokeStat(baseComponent.BaseComponent):
    DEFAULT_MODIFIER_VALUE = 2
    DEFAULT_MODIFIER_MAX = 8

    IV_CAP = 31
    EV_CAP = 252

    FAVORABLE_NATURE_BONUS = 1.10
    NON_FAVORABLE_NATURE_BONUS = 0.90

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(int(node.value))

    def __init__(self, baseStat: int = 1):
        """ Contains the lowest-level stat functions for any monster stat, either battle or otherwise
        :param int baseStat: This is the minimum stat a monster can naturally have, outside of stat modifiers
        """

        self.baseStat = baseStat

        self.modifierNumerator = self.DEFAULT_MODIFIER_VALUE
        self.modifierDenominator = self.DEFAULT_MODIFIER_VALUE

        self._rawValue = None
        self._level = 1
        self._effortValues = 0
        self._innateValue = None
        self.natureMultiplier = 1.00

    @property
    def effortValues(self) -> int:
        """ Get the effort values of this stat instance. These add +1 the stat's value for every 4 obtained
        """

        return self._effortValues

    @effortValues.setter
    def effortValues(self, newEffortValues: int):
        # Since EVs matter only for every 4 collected, force a new rawValue calculation for every 4 EVs gained
        if not newEffortValues % 4:
            self._rawValue = None

        self._effortValues = min(newEffortValues, self.EV_CAP)

    @property
    def innateValue(self) -> int:
        """ Which value a stat instance "naturally" has. Generated from a random range when none is already defined
        """

        if self._innateValue is not None:
            return self._innateValue

        self._innateValue = random.randrange(0, self.IV_CAP + 1)
        return self._innateValue

    @innateValue.setter
    def innateValue(self, newValue) -> int:
        self._innateValue = min(newValue, self.IV_CAP)

    @property
    def level(self) -> int:
        """ Get the level of this stat, inherited from the monster it's assigned to
        """

        return self._level

    @level.setter
    def level(self, newLevel: int):
        """ Force a new calculation for this stat whenever it's level changes. Ensures stats remain up-to-date
        """

        self._level = newLevel
        self._rawValue = None

    @property
    def rawValue(self) -> int:
        """ The current stat before status changes, calculated for IVs, EVs, current level and nature
        """

        # Lazy load it once so we don't recalculate it every time it's called
        if self._rawValue is not None:
            return self._rawValue

        self._rawValue = (((2 * self.baseStat) + self.innateValue +
                           (self.effortValues - self.effortValues % 4) // 4) * self.level) / 100

        self._rawValue += 5
        self._rawValue = self._rawValue * self.natureMultiplier

        return int(self._rawValue)

    @property
    def combatValue(self) -> int:
        """ The value of the raw stat multiplied by the current stat modifiers
        """

        return self.rawValue * (self.modifierNumerator // self.modifierDenominator)

    def applyModifier(self, modifierOffset: int = 0):
        """ Apply an offset to this stat. These have a total of 12 stages, +6 to -6
        :param modifierOffset: How many stages we want the new stat to be offset by
        """

        def processModifier(primaryModifier: int, secondaryModifier: int, targetOffset: int) -> tuple[int, int]:
            """ Process the modifiers according to a priority system
            """

            positiveOffset = abs(targetOffset)
            currentPrimaryOffset = primaryModifier - self.DEFAULT_MODIFIER_VALUE

            if currentPrimaryOffset >= positiveOffset:
                if targetOffset < 0:
                    targetOffset = positiveOffset
                return primaryModifier - targetOffset, secondaryModifier

            primaryModifier -= currentPrimaryOffset
            remainingOffset = positiveOffset - currentPrimaryOffset
            return primaryModifier, min(secondaryModifier + remainingOffset, self.DEFAULT_MODIFIER_MAX)

        # Negative stat changes, lower numerator before  raising denominator
        if modifierOffset < 0:
            self.modifierNumerator, self.modifierDenominator = processModifier(
                self.modifierNumerator,
                self.modifierDenominator,
                modifierOffset
            )
            return

        # Positive stat changes, lower denominator before raising numerator
        self.modifierDenominator, self.modifierNumerator = processModifier(
            self.modifierDenominator,
            self.modifierNumerator,
            modifierOffset
        )


class HealthPoints(PokeStat):
    yaml_tag = '!stat_HealthPoints'

    @property
    def rawValue(self) -> int:
        if self._rawValue is not None:
            return self._rawValue

        self._rawValue = (((2 * self.baseStat) + self.innateValue + (self.effortValues // 4)) * self.level) // 100

        self._rawValue += (self.level + 10)
        return int(self._rawValue)


class Attack(PokeStat):
    yaml_tag = '!stat_Attack'


class Defense(PokeStat):
    yaml_tag = '!stat_Defense'


class Special(PokeStat):
    yaml_tag = '!stat_Special'


class SpecialAttack(PokeStat):
    yaml_tag = '!stat_SpecialAttack'


class SpecialDefense(PokeStat):
    yaml_tag = '!stat_SpecialDefense'


class Speed(PokeStat):
    yaml_tag = '!stat_Speed'


class Evasion(PokeStat):
    yaml_tag = '!stat_Evasion'


class Accuracy(PokeStat):
    yaml_tag = '!stat_Accuracy'
