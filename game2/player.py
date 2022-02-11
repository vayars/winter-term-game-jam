class Player():
    # The player class. Contains the player's inventory.
    def __init__(self):
        self.inventory = []

    def addInventory(self, item):
        self.inventory.append(item)
        return True
    
    def removeInventory(self, item):
        temp = self.inventory.remove(item)
        return temp

    def getInventory(self):
        return self.inventory

    def isEmpty(self):
        if len(self.inventory) == 0:
            return True
        else:
            return False

    def printInventory(self):
        if self.isEmpty():
            print("\nYour inventory is empty.")
        else:
            print("\nYou currently have:")
            for ind in range(0,len(self.inventory)):
                print("- " + self.inventory[ind].getID())