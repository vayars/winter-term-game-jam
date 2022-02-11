class Cage():
    # The cage which holds the chalice that ends the game. It's connected to the four colored doors.
    def __init__(self):
        self.id = "Golden Cage"
        self.desc4Lock = "There are four locked locks on the birdcage: one orange, one green, \none purple, and one pink. There are no noticeable key holes. Inside \nsits a glimmering chalice. "
        self.desc3Lock = "There is one unlocked lock and three locked locks on the birdcage: \none orange, one green, one purple, and one pink. There are no noticeable \nkey holes. Inside sits a glimmering chalice. "
        self.desc2Lock = "There are two unlocked locks and three locked locks on the birdcage: \none orange, one green, one purple, and one pink. There are no noticeable \nkey holes. Inside sits a glimmering chalice."
        self.desc1Lock = "There are three unlocked locks and one locked lock on the birdcage: \none orange, one green, one purple, and one pink. There are no noticeable \nkey holes. Inside sits a glimmering chalice."
        self.descUnlocked = "There are four unlocked locks on the birdcage: one orange, one green, \none purple, and one pink. There are no noticeable key holes. Inside \nsits a glimmering chalice."
        self.locks = 4
        self.actionsLocked = ["Go back."]
        self.actionsUnlocked = ["Take the glimmering chalice.", "Go back."]

    def getID(self):
        return self.id

    def getDesc(self):
        if self.locks == 4:
            return self.desc4Lock
        elif self.locks == 3:
            return self.desc3Lock
        elif self.locks == 2:
            return self.desc2Lock
        elif self.locks == 1:
            return self.desc1Lock
        elif self.locks == 0:
            return self.descUnlocked
        else:
            return "Oops! Something went wrong."

    def getActions(self):
        if self.locks == 0:
            return self.actionsUnlocked
        else:
            return self.actionsLocked

    def unlockLock(self):
        self.locks -= 1
        return self.locks

    def isUnlocked(self):
        if self.locks == 0:
            return True
        else:
            return False
