# -----------------------------------------------------------#
# Created by willderose                             #
# -----------------------------------------------------------#

from pokeComponents import baseComponent


class PokeType(baseComponent.BaseComponent):
    """ Since we need all the pokeTypes to be aware of each other, but don't need instances for each
    store the various weaknesses, resistances and immunities in a static method
    """

    displayColor: str

    @classmethod
    def from_yaml(cls, loader, node):
        return cls

    @staticmethod
    def immunities() -> list['PokeType']:
        """ Types placed here have no effect in battle against the type it's assigned to
        """

        pass

    @staticmethod
    def resistances() -> list['PokeType']:
        """ Types here are resisted in battle against the type it's assigned to
        """

        pass

    @staticmethod
    def weaknesses() -> list['PokeType']:
        """ Types listed here are stronger in battle against the type it's assigned to
        """

        pass


class Bug(PokeType):
    yaml_tag = '!type_Bug'

    @staticmethod
    def resistances():
        return [Fighting, Grass, Ground]

    @staticmethod
    def weaknesses():
        return [Fire, Flying, Poison, Rock]


class Dark(PokeType):
    yaml_tag = '!type_Dark'

    @staticmethod
    def resistances():
        return [Dark, Ghost]

    @staticmethod
    def weaknesses():
        return [Bug, Fighting]

    @staticmethod
    def immunities():
        return [Psychic]


class Dragon(PokeType):
    yaml_tag = '!type_Dragon'

    @staticmethod
    def resistances():
        return [Electric, Fire, Grass, Water]

    @staticmethod
    def weaknesses():
        return [Dragon, Ice]


class Electric(PokeType):
    yaml_tag = '!type_Electric'

    @staticmethod
    def resistances():
        return [Electric, Flying]

    @staticmethod
    def weaknesses():
        return [Ground]


class Fairy(PokeType):
    yaml_tag = '!type_Fairy'

    @staticmethod
    def resistances():
        return [Bug, Dark, Fighting]

    @staticmethod
    def weaknesses():
        return [Poison, Steel]

    @staticmethod
    def immunities():
        return [Dragon]


class Fighting(PokeType):
    yaml_tag = '!type_Fighting'

    @staticmethod
    def resistances():
        return [Bug, Rock]

    @staticmethod
    def weaknesses():
        return [Flying, Psychic]


class Fire(PokeType):
    yaml_tag = '!type_Fire'

    @staticmethod
    def resistances():
        return [Bug, Fire, Grass]

    @staticmethod
    def weaknesses():
        return [Ground, Rock, Water]


class Flying(PokeType):
    yaml_tag = '!type_Flying'

    @staticmethod
    def resistances():
        return [Bug, Fighting, Grass]

    @staticmethod
    def weaknesses():
        return [Electric, Ice, Rock]

    @staticmethod
    def immunities():
        return [Ground]


class Ghost(PokeType):
    yaml_tag = '!type_Ghost'

    @staticmethod
    def resistances():
        return [Bug, Poison]

    @staticmethod
    def weaknesses():
        return [Dark, Ghost]

    @staticmethod
    def immunities():
        return [Normal, Fighting]


class Grass(PokeType):
    yaml_tag = '!type_Grass'

    @staticmethod
    def resistances():
        return [Electric, Grass, Ground, Water]

    @staticmethod
    def weaknesses():
        return [Bug, Fire, Flying, Ice, Poison]


class Ground(PokeType):
    yaml_tag = '!type_Ground'

    @staticmethod
    def resistances():
        return [Poison, Rock]

    @staticmethod
    def weaknesses():
        return [Grass, Ice, Water]

    @staticmethod
    def immunities():
        return [Electric]


class Ice(PokeType):
    yaml_tag = '!type_Ice'

    @staticmethod
    def resistances():
        return [Ice]

    @staticmethod
    def weaknesses():
        return [Fighting, Fire, Rock, Steel]


class Normal(PokeType):
    yaml_tag = '!type_Normal'

    @staticmethod
    def weaknesses():
        return [Fighting]

    @staticmethod
    def immunities():
        return [Ghost]


class Poison(PokeType):
    yaml_tag = '!type_Poison'

    @staticmethod
    def resistances():
        return [Fighting, Poison, Grass, Bug, Fairy]

    @staticmethod
    def weaknesses():
        return [Ground, Psychic]


class Psychic(PokeType):
    yaml_tag = '!type_Psychic'

    @staticmethod
    def resistances():
        return [Fighting, Psychic]

    @staticmethod
    def weaknesses():
        return [Bug, Dark, Ghost]


class Rock(PokeType):
    yaml_tag = '!type_Rock'

    @staticmethod
    def resistances():
        return [Fire, Flying, Normal, Poison]

    @staticmethod
    def weaknesses():
        return [Fighting, Grass, Ground, Steel, Water]


class Steel(PokeType):
    yaml_tag = '!type_Steel'

    @staticmethod
    def resistances():
        return [Bug, Dragon, Fairy, Flying, Grass, Ice, Normal, Psychic, Rock, Steel]

    @staticmethod
    def weaknesses():
        return [Fighting, Fire, Ground]

    @staticmethod
    def immunities():
        return [Poison]


class Water(PokeType):
    yaml_tag = '!type_Water'

    @staticmethod
    def resistances():
        return [Fire, Ice, Water]

    @staticmethod
    def weaknesses():
        return [Electric, Grass]
