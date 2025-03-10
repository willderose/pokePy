# -----------------------------------------------------------#
# Created by William Desrosiers                              #
# -----------------------------------------------------------#
import pytest
from typing import Type

import pokeComponents.pokeStats


@pytest.fixture()
def statInstance() -> Type['pokeComponents.pokeStats.PokeStat']:
    """ Create a pokeStat instance for use in the tests
    """

    return pokeComponents.pokeStats.PokeStat()
