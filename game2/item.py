class Item():
    # A generic class for every item. Contains an ID, a description, and a
    # list of possible actions.
    def __init__(self,id):
        self.id = id
        self.desc = ""
        self.actions = ["Take it with you.", "Go back."]

    def getID(self):
        return self.id

    def getDesc(self):
        return self.desc
    
    def setDesc(self, new_desc):
        self.desc = new_desc
        return self.desc

    def getActions(self):
        return self.actions