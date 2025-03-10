# -----------------------------------------------------------#
# Created by William Desrosiers                              #
# -----------------------------------------------------------#


def test_componentEnginRequest():

    from systems.componentEngine import ComponentEngine

    asdf = ComponentEngine()
    asdf.findComponentTypes()
    testPoke = asdf.requestInstanceOfComponent('!pokeMonster_testMon')
    import pprint
    pprint.pprint(testPoke)