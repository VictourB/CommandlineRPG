import sys, random
from entity import Entity
import settings


class Player(Entity):
    def __init__(self, name,description,hp,mp,atk,dfs,spd) -> None:
        super().__init__(name,description,hp,mp,atk,dfs,spd)

    def use_item(self):
        self.inv = settings.spoils_DSC
        print("Your Items:")
        for key in self.inv:
            print(key)

        print("Which Item would you like to use?")
        response = input()
        for key in self.inv:
            if response.capitalize() == key:
                print()
                print("Using item!")
                print(self.inv[key])
                match key:
                    case "Food":
                        pass
                    case "Water":
                        pass
                    case "Donut":
                        pass
                    case "EMP":
                        pass
                    case "Smelly Spray":
                        pass
                    case "Blank Check":
                        pass
                    case "Gun":
                        pass
                    case "Book":
                        pass
                    case "Energy Drink":
                        pass
                    case _:
                        pass






    def die():
        print("""
        
    YOU HAVE DIED!
    It's a tough world out there and you weren't able to make it. 
    Now your bones litter the wayside and your existence is slowly forgotten.
    Perhaps if things were different, and you were in another time or place.
    If you wish your soul may try again.
        
        """)
        if input():                                                             # TODO: Go back to main menu instead of exiting
            sys.exit()
        

