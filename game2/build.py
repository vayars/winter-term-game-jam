from tkinter import Y
from xml.etree.ElementTree import tostring
import constants
import room
import door

from cage import Cage
from item import Item
from room import Room

class Build():
    # Builds the levels of the game.
    def __init__(self):
        pass

    def buildSmall(self):
        items_array = []
        rooms_array = []
        doors_array = []

        # Create items and add to the items_array.
        red_key = Item("Red Key")
        yellow_key = Item("Yellow Key")
        blue_key = Item("Blue Key")
        white_key = Item("White Key")
        bird_cage = Cage()

        red_key.setDesc("You find an old, red key.")
        yellow_key.setDesc("You find an old, yellow key.")
        blue_key.setDesc("You find an old, blue key.")
        white_key.setDesc("You find an old, white key.")

        items_array.append(red_key)
        items_array.append(yellow_key)
        items_array.append(blue_key)
        items_array.append(white_key)
        items_array.append(bird_cage)

        # Create rooms and add to the rooms_array.
        for i in range(9):
            new_room = Room(i)
            rooms_array.append(new_room)
        
        rooms_array[0].setDesc("A plain looking room. There's a pile of rubble in the middle of the \nroom. To the east and south are two doors.")
        rooms_array[1].setDesc("A very crumbled and old-looking room. There's a pile of rotted wood in \none corner. To the east and west are two doors. To the south, there's \na pink door with two key holes.")
        rooms_array[2].setDesc("A room which likely used to store food. Unfortunately, most of it is \ngone, and all that's left are the shelves and cobwebs. To the south and \nwest are two doors.")
        rooms_array[3].setDesc("A sitting room. There are stone chairs scattered about. To the north and \nsouth are two doors. To the east, there's an orange door with two key \nholes.")
        rooms_array[4].setDesc("An elaborately decorated room. While most of the furniture has \nunfortunately rusted, there is a stone pedestal in the middle. On the \npedestal sits a birdcage containing a shining, golden chalice. There \nis a pink door to the north, a purple door to the east, a green door to \nthe south, and an orange door to the west. All four doors have two \nkey holes each.")
        rooms_array[5].setDesc("An empty-looking room, save for a single wooden cabinet. To the north \nand south are two doors. To the west, there's a purple door with two \nkey holes.")
        rooms_array[6].setDesc("A room which might've been a bedroom at some point. The bed is covered \nin a layer of dust. To the north and east are two doors.")
        rooms_array[7].setDesc("A room filled with empty weapon racks. The spears and bows that may \nhave been housed here are gone. To the east and west are two doors. \nTo the north, there's a green door with two key holes.")
        rooms_array[8].setDesc("A drawing room. There are shelves of delicate sheet music which could \ndisolve under the lightest touch. To the north and west are two doors.")

        # Create doors and add to the doors_array.
        normal = door.Door(constants.NORMAL)
        orange = door.Door(constants.ORANGE, red_key, yellow_key)
        green = door.Door(constants.GREEN, yellow_key, blue_key)
        purple = door.Door(constants.PURPLE, red_key, blue_key)
        pink = door.Door(constants.PINK, red_key, white_key)
        
        normal.setDescUnlocked("In front of you is a normal, unlocked door.")
        orange.setDescLocked("In front of you is a locked orange door.")
        orange.setDescUnlocked("In front of you is an unlocked orange door.")
        green.setDescLocked("In front of you is a locked green door.")
        green.setDescUnlocked("In front of you is an unlocked green door.")
        purple.setDescLocked("In front of you is a locked purple door.")
        purple.setDescUnlocked("In front of you is an unlocked purple door.")
        pink.setDescLocked("In front of you is a locked pink door.")
        pink.setDescUnlocked("In front of you is an unlocked pink door.")

        doors_array.append(normal)
        doors_array.append(orange)
        doors_array.append(green)
        doors_array.append(purple)
        doors_array.append(pink)

        # Add items to rooms.
        rooms_array[0].addItem(red_key)
        rooms_array[1].addItem(yellow_key)
        rooms_array[2].addItem(blue_key)

        rooms_array[3].addItem(yellow_key)
        rooms_array[4].addItem(bird_cage)
        rooms_array[5].addItem(white_key)

        rooms_array[6].addItem(red_key)
        rooms_array[7].addItem(red_key)
        rooms_array[8].addItem(blue_key)

        # Add adjecent rooms to rooms based on their index in the rooms array.
        rooms_array[0].setExits(-1,1,3,-1)
        rooms_array[1].setExits(-1,2,4,0)
        rooms_array[2].setExits(-1,-1,5,1)

        rooms_array[3].setExits(0,4,6,-1)
        rooms_array[4].setExits(1,5,7,3)
        rooms_array[5].setExits(2,-1,8,4)

        rooms_array[6].setExits(3,7,-1,-1)
        rooms_array[7].setExits(4,8,-1,6)
        rooms_array[8].setExits(5,-1,-1,7)

        # Add doors to rooms based on their index in the doors_array.
        # -1 = no door
        # 0 = normal
        # 1 = orange
        # 2 = green
        # 3 = purple
        # 4 = pink
        rooms_array[0].setDoors(-1,0,0,-1)
        rooms_array[1].setDoors(-1,0,4,0)
        rooms_array[2].setDoors(-1,-1,0,0)

        rooms_array[3].setDoors(0,1,0,-1)
        rooms_array[4].setDoors(4,3,2,1)
        rooms_array[5].setDoors(0,-1,0,3)

        rooms_array[6].setDoors(0,0,-1,-1)
        rooms_array[7].setDoors(2,0,-1,0)
        rooms_array[8].setDoors(0,-1,-1,0)

        # Return the list of items, rooms, and doors.
        return items_array, rooms_array, doors_array