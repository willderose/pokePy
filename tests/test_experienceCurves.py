# -----------------------------------------------------------#
# Created by William Desrosiers                              #
# -----------------------------------------------------------#

def test_Erratic():
    from pokeComponents import experienceCurves

    level = 12
    assert experienceCurves.Erratic.getRequiredXPForLevel(level) == 3041
    assert experienceCurves.Erratic.getRequiredXpForNextLevel(level) == 781

    level = 55
    assert experienceCurves.Erratic.getRequiredXPForLevel(level) == 158056
    assert experienceCurves.Erratic.getRequiredXpForNextLevel(level) == 7023

    level = 75
    assert experienceCurves.Erratic.getRequiredXPForLevel(level) == 326531
    assert experienceCurves.Erratic.getRequiredXpForNextLevel(level) == 9724

    level = 99
    assert experienceCurves.Erratic.getRequiredXPForLevel(level) == 591882
    assert experienceCurves.Erratic.getRequiredXpForNextLevel(level) == 8118


def test_Fast():
    from pokeComponents import experienceCurves

    level = 50

    assert experienceCurves.Fast.getRequiredXPForLevel(level) == 100000
    assert experienceCurves.Fast.getRequiredXpForNextLevel(level) == 6120


def test_Fluctuating():
    from pokeComponents import experienceCurves

    level = 12

    assert experienceCurves.Fluctuating.getRequiredXPForLevel(level) == 967
    assert experienceCurves.Fluctuating.getRequiredXpForNextLevel(level) == 263

    level = 32

    assert experienceCurves.Fluctuating.getRequiredXPForLevel(level) == 30146
    assert experienceCurves.Fluctuating.getRequiredXpForNextLevel(level) == 3634

    level = 50

    assert experienceCurves.Fluctuating.getRequiredXPForLevel(level) == 142500
    assert experienceCurves.Fluctuating.getRequiredXpForNextLevel(level) == 8722


def test_MediumFast():
    from pokeComponents import experienceCurves

    level = 50

    assert experienceCurves.MediumFast.getRequiredXPForLevel(level) == 125000
    assert experienceCurves.MediumFast.getRequiredXpForNextLevel(level) == 7651


def test_MediumSlow():
    from pokeComponents import experienceCurves

    level = 50

    assert experienceCurves.MediumSlow.getRequiredXPForLevel(level) == 117360
    assert experienceCurves.MediumSlow.getRequiredXpForNextLevel(level) == 7766


def test_Slow():
    from pokeComponents import experienceCurves

    level = 50

    assert experienceCurves.Slow.getRequiredXPForLevel(level) == 156250
    assert experienceCurves.Slow.getRequiredXpForNextLevel(level) == 9563
