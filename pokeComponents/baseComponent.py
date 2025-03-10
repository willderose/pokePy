# -----------------------------------------------------------#
# Created by willderose                                      #
# -----------------------------------------------------------#
import yaml


class BaseComponent(yaml.YAMLObject):
    """ Base component class that'll offer the lowest level methods and attributes for all of pokePy's component types
    """

    yaml_tag = None

    @classmethod
    def from_yaml(cls, loader, node):
        raise NotImplementedError('from_yaml not implemented in {}'.format(cls.__name__))

    @classmethod
    def name(cls) -> str:
        """ Simple convenience method to get the name of this class"""
        return cls.__name__

    @classmethod
    def loadFromSavedYaml(self, *args, **kwargs):
        return NotImplementedError('loadFromSavedYaml not implemented in {}'.format(self.__class__.__name__))
