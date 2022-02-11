import constants
from item import Item

class Door():
    # A generic class for every door. Contains the door's color/type,
    # whether it's locked/unlocked, and which keys are needed to open it.
    def __init__(self, color, key1 = None, key2 = None, key3 = None):
        self.color = color
        self.unlocked = False
        if color == constants.NORMAL:
            self.unlocked = True

        self.desc_locked = ""
        self.desc_unlocked = ""

        self.key_one = key1
        self.key_two = key2
        self.key_three = key3

        self.actionsLocked = ["Attempt to unlock door.", "Check inventory.", "Go back."]
        self.actionsUnlocked = ["Go to next room.", "Check inventory.", "Go back."]

    def getColor(self):
        return self.color

    def setDescLocked(self, new_desc):
        self.desc_locked = new_desc
        return True

    def setDescUnlocked(self, new_desc):
        self.desc_unlocked = new_desc
        return True

    def getDesc(self):
        if self.unlocked:
            return self.desc_unlocked
        else:
            return self.desc_locked
    
    def isUnlocked(self):
        return self.unlocked

    def containsKey(self, inventory, key):
        contains = False
        for i in range(len(inventory)):
            if inventory[i] == key:
                contains = True
                break
        return contains

    # Checks which keys are needed to unlock the door and if the player has
    # those keys in their inventory. If yes, it removes the keys from the
    # player's inventory and becomes unlocked. If no, it remains locked.
    def tryUnlock(self, inventory):
        if isinstance(self.key_one, Item):
            if isinstance(self.key_two, Item):
                if isinstance(self.key_three, Item):
                    if self.containsKey(inventory,self.key_one) and self.containsKey(inventory,self.key_two) and self.containsKey(inventory,self.key_three):
                        inventory.remove(self.key_one)
                        inventory.remove(self.key_two)
                        inventory.remove(self.key_three)
                        self.unlocked = True
                else:
                    if self.containsKey(inventory,self.key_one) and self.containsKey(inventory, self.key_two):
                        inventory.remove(self.key_one)
                        inventory.remove(self.key_two)
                        self.unlocked = True
            else:
                if self.containsKey(inventory,self.key_one):
                    inventory.remove(self.key_one)
                    self.unlocked = True
        return self.unlocked

    def getActions(self):
        if self.unlocked:
            return self.actionsUnlocked
        else:
            return self.actionsLocked

    