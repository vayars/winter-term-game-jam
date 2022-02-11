from multiprocessing.sharedctypes import Value
from build import Build
from door import Door
from cage import Cage
from item import Item
from player import Player
from room import Room


class Main():
    def main():
        # Build the map.
        player = Player()
        builder = Build()
        items, rooms, doors = builder.buildSmall()
        game_done = False
        print("You are an archeologist searching nearby ruins for guarded treasurer. \nOn one of your expeditons, however, you were seperated from your team \nby an earthquake! Upon awaking, you noticed that you were deep \nunderground and a mysterious and unkonwn ruin. After getting your \nbearings, it's time to try and find a way out!")

        # Game loop.
        curr_room = rooms[0]
        curr_focus = rooms[0]
        curr_dir = -1

        while(not game_done):
            # Print Focus Description
            print()
            print(curr_focus.getDesc())
            # Player input loop
            given_input = False
            p_input = -1
            while(not given_input):
                print("\nWhat will you do?")
                for i in range(len(curr_focus.getActions())):
                    print(str(i+1) + ": " + curr_focus.getActions()[i])
                try:
                    p_input = int(input("Choice: "))-1
                    if p_input < 0 or p_input > len(curr_focus.getActions()):
                        raise ValueError
                except(ValueError):
                    print("\nYou can't do that. Please enter a number between 1 and 5.")
                    continue
                given_input = True
                
            # Update environment based on input
            if isinstance(curr_focus, Room):
                match p_input:
                    case 0: # Investigate the room.
                        if len(curr_focus.getItems()) > 0:
                            curr_focus = curr_focus.getItem(0)
                        else:
                            print("\nThere is nothing else of interest in this room.")
                    case 1: # Look north
                        curr_dir = 0
                        if curr_focus.getDoor(0) == -1:
                            print("\nIn front of you is an empty wall.")
                        else:
                            curr_focus = doors[curr_focus.getDoor(0)]
                    case 2: # Look east
                        curr_dir = 1
                        if curr_focus.getDoor(1) == -1:
                            print("\nIn front of you is an empty wall.")
                        else:
                            curr_focus = doors[curr_focus.getDoor(1)]
                    case 3: # Look south
                        curr_dir = 2
                        if curr_focus.getDoor(2) == -1:
                            print("\nIn front of you is an empty wall.")
                        else:
                            curr_focus = doors[curr_focus.getDoor(2)]
                    case 4: # Look west
                        curr_dir = 3
                        if curr_focus.getDoor(3) == -1:
                            print("\nIn front of you is an empty wall.")
                        else:
                            curr_focus = doors[curr_focus.getDoor(3)]
                    case 5:
                        player.printInventory()
            elif isinstance(curr_focus, Door):
                match p_input:
                    case 0:
                        if curr_focus.isUnlocked(): # Set the room and the focus to the next room.
                             if curr_dir == -1:
                                 print("\nOops! Something went wrong.")
                             curr_room = rooms[curr_room.getExit(curr_dir)]
                             curr_focus = curr_room
                             curr_dir = -1
                        else:
                            result = curr_focus.tryUnlock(player.getInventory())
                            if result:
                                print("\nThe door unlocks.")
                                items[4].unlockLock()
                            else:
                                print("\nYou don't seem to have the right keys in your inventory.")
                    case 1:
                        player.printInventory()
                    case 2:
                        curr_focus = curr_room
                        curr_dir = -1
            elif isinstance(curr_focus, Item):
                match p_input:
                    case 0:
                        print("\nYou gained " + curr_focus.getID() + ".")
                        player.addInventory(curr_room.removeItem(0))
                        curr_focus = curr_room
                    case 1:
                        curr_focus = curr_room
            elif isinstance(curr_focus, Cage):
                match p_input:
                    case 0:
                        if curr_focus.isUnlocked(): # End the game
                            print("\nYou gained " + curr_focus.getID() + ".")
                            game_done = True
                            break
                        else:
                            curr_focus = curr_room
                    case 1:
                        curr_focus = curr_room
        print("\nUpon grabbing the chalice, you are engulfed in a flash of light. You \nappear back where you were before the earthquake with the chalice still \nin your hands. It shines in the sunlight as you make your way back to \nyour camp, excited to share your discovery with your colleagues.")
        print("\nThank you for playing! \nCreated by Veronica Ayars")

Main.main()