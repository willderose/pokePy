# -----------------------------------------------------------#
# Created by willderose                              #
# -----------------------------------------------------------#


class PokeActor(object):
    """ Base class fo all actors (NPCs and Player)
    """

    def __init__(self):
        self.name = None
        self.inventory = None
        self.team = None

