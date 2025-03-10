# -----------------------------------------------------------#
# Created by William Desrosiers                              #
# -----------------------------------------------------------#
import importlib
import inspect
import os
import pkgutil
import logging

import yaml

import pokeComponents

from systems import pokeLogging


class ComponentEngine:
    """ The component engine lets us define and request various components of this project for later use(s)
    """

    DATA_BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

    def __init__(self, logLevel=logging.DEBUG):
        if not os.path.exists(self.DATA_BASE_PATH):
            raise RuntimeError('No data path exists in this app. Expected: {}'.format(self.DATA_BASE_PATH))

        self.logger = pokeLogging.createLogger(ComponentEngine.__name__)
        self.logger.setLevel(logLevel)

        self._componentFilesByTag = {}
        self.componentSources = {}

        self.componentLoader = yaml.SafeLoader

    def findComponentTypes(self):
        """ Iterate through the pokeComponent modules and find all the component types so we can register them on this
        class for later use
        """

        for moduleInfo in pkgutil.walk_packages([os.path.dirname(pokeComponents.__file__)]):
            self.logger.debug('Finding valid component classes in {}'.format(moduleInfo.name))
            self.registerComponentsInModule(
                importlib.import_module(
                    'pokeComponents.' + moduleInfo.name
                )
            )

        for componentDir in os.listdir(ComponentEngine.DATA_BASE_PATH):
            self.logger.debug('Finding component files under {}'.format(componentDir))
            self.registerComponentsFromDir(os.path.join(ComponentEngine.DATA_BASE_PATH, componentDir))

    def registerComponentsFromDir(self, dirName: str):
        """ Register the components from the supplied directory under their appropriate type
        """

        if not self.componentSources:
            raise RuntimeError('No python sources to base the components around')

        componentType = os.path.basename(dirName)
        for componentFile in os.listdir(dirName):
            componentFilePath = os.path.join(dirName, componentFile)
            componentTag = self.getComponentTagFromFile(componentFilePath)
            self._componentFilesByTag[componentTag] = componentFilePath
            self.componentLoader.add_constructor(componentTag, self.getComponentFromFile)
            self.logger.debug('Registered {} of type {} with tag {}'.format(componentFile, componentType, componentTag))

    def registerComponentsInModule(self, module):
        """ Register the components (those with a valid yaml_tag class attribute) to this class' loader for future use
        """

        for className, classObject in inspect.getmembers(module, inspect.isclass):
            componentTag = getattr(classObject, 'yaml_tag', '') or ''
            if not componentTag.startswith('!'):
                self.logger.error('  Missing or invalid YAML tag on object {}'.format(className))
                continue

            self.componentSources[componentTag] = classObject
            self.componentLoader.add_constructor(classObject.yaml_tag, classObject.from_yaml)
            self.logger.debug('  Registered component {} with tag {}'.format(className, classObject.yaml_tag))

    def requestInstanceOfComponent(self, componentTag: str):
        """ Create an instance of the desired component. This name must be registered prior to the request.
        See ComponentEngine.findComponentTypes

        :return: An instance of the desired component's name. This will vary depending on which component is requested
        """

        componentYaml = self._componentFilesByTag[componentTag]
        with open(componentYaml, 'r') as yamlBuffer:
            return yaml.load(yamlBuffer, Loader=self.componentLoader)

    def getComponentFromFile(self, loader, node):
        """ Get a component from the tag defined in a file. This allows various yaml files to inherit each other
        """

        mappingTag = node.tag
        componentInstance = self.requestInstanceOfComponent(mappingTag)
        if node.value:
            componentInstance.loadFromSavedYaml(**loader.construct_mapping(node, deep=True))

        return componentInstance

    @staticmethod
    def getComponentTagFromFile(filePath: str) -> str:
        """ Build a yaml tag that from the supplied yaml file path
        Prefix them with the directory name in case there are conflicting file names.
        """

        return '!{}_{}'.format(
            os.path.basename(os.path.dirname(filePath)),
            os.path.basename(os.path.splitext(filePath)[0])
        )
