import constants

class Room():
    # A generic class for every room. Contains the room number, a description,
    # a list of items in the room, a list of doors in the room, a list of
    # adjecent rooms, and a list of possible actions.
    def __init__(self, number):
        self.room = number
        self.desc = ""
        self.items = []
        self.doors = [-1,-1,-1,-1]
        self.exits = [-1,-1,-1,-1]
        self.actions = ["Look for objects.","Examine north wall.","Examine east wall.", "Examine south wall.", "Examine west wall.", "Check inventory."]
    
    def setDesc(self, new_desc):
        self.desc = new_desc
        return True
    
    def getDesc(self):
        return self.desc

    def addItem(self, item):
        self.items.append(item)
        return True

    def removeItem(self, index):
        item = self.items[index]
        self.items.remove(item)
        return item

    def getItems(self):
        return self.items

    def getItem(self, index):
        return self.items[index]

    def setExits(self, north, east, south, west):
        self.exits[0] = north
        self.exits[1] = east
        self.exits[2] = south
        self.exits[3] = west
        return True

    def getExits(self):
        return self.exits
    
    def getExit(self, direction):
        return self.exits[direction]

    def setDoors(self, north, east, south, west):
        self.doors[0] = north
        self.doors[1] = east
        self.doors[2] = south
        self.doors[3] = west
        return True

    def getDoors(self):
        return self.doors

    def getDoor(self, direction):
        return self.doors[direction]

    def getActions(self):
        return self.actions