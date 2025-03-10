# -----------------------------------------------------------#
# Created by William Desrosiers                              #
# -----------------------------------------------------------#


def test_combatValue(statInstance):
    statInstance.level = 50
    statInstance._innateValue = 0

    statInstance.applyModifier(4)
    assert statInstance.combatValue == 18

    statInstance.applyModifier(-4)
    assert statInstance.combatValue == 6


def test_effortValueChanges(statInstance):
    for i in range(310):
        statInstance.effortValues += 1
    assert statInstance.effortValues == 252


def test_healthGrowth():
    """ Validate the growth of the Health Point stat, who has a different growth compared to the other stats
    """
    from pokeComponents import pokeStats

    hP = pokeStats.HealthPoints(70)
    hP.level = 50
    hP._innateValue = 24
    hP.effortValues = 74

    assert hP.rawValue == 151


def test_statGrowthWithNatureBonus(statInstance):
    """ Test the stat growth of a favorable stat at arbitrary innate, effort and base stat values
    """
    statInstance.natureMultiplier = statInstance.FAVORABLE_NATURE_BONUS
    statInstance.baseStat = 77
    statInstance.level = 50
    statInstance.effortValues = 52
    statInstance._innateValue = 13

    assert statInstance.rawValue == 104


def test_statGrowthWithoutNatureBonus(statInstance):
    """ Test the stat growth of a non-favored stat at arbitrary innate, effort and base stat values
    """
    statInstance.natureMultiplier = statInstance.NON_FAVORABLE_NATURE_BONUS
    statInstance.baseStat = 77
    statInstance.level = 50
    statInstance.effortValues = 52
    statInstance._innateValue = 13

    assert statInstance.rawValue == 85


def test_validateIVRange(statInstance):
    for i in range(20):
        assert statInstance.innateValue <= statInstance.IV_CAP + 1


def test_validateStatChanges(statInstance):
    statInstance.applyModifier(2)

    assert statInstance.modifierNumerator / statInstance.modifierDenominator == 2.0

    statInstance.applyModifier(-4)

    assert statInstance.modifierNumerator / statInstance.modifierDenominator == 0.5

    statInstance.applyModifier(5)
    assert statInstance.modifierNumerator / statInstance.modifierDenominator == 2.5
