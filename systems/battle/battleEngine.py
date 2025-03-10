# -----------------------------------------------------------#
# Created by William Desrosiers                              #
# -----------------------------------------------------------#

from . import battleField


class BattleEngine(object):
    VALID_BATTLE_HOOKS = [
        'turnEnd',
        'turnStart',
        'switchIn',
        'switchOut',
    ]

    def __init__(self):
        self.hooks = {hookName: {} for hookName in self.VALID_BATTLE_HOOKS}
        self.turnCount = 0

        self.actionQueue = []

    def processHooksForName(self, hookName: str):
        for hook in self.hooks.get(hookName, []):
            hook()

    def processTurn(self):
        """ Process the actions currently stored in the action queue
        """

        self.processHooksForName('turnStart')

        for actionPriority, action, actionKwargs in sorted(self.actionQueue, key=lambda actionMeta: actionMeta[0]):
            action(**actionKwargs)

        self.turnCount += 1

        self.processHooksForName('turnEnd')
