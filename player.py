import sys, random
from entity import Entity
import settings


class Player(Entity):
    def __init__(self, name,description,hp,mp,atk,dfs,spd) -> None:
        super().__init__(name,description,hp,mp,atk,dfs,spd)
        self.inv = settings.spoils_DSC

    def attack(self, enemy):
        damage = self.current_atk - enemy.current_dfs
        if damage < 0:
            damage = 0
        print(f"\n{self.name} attacked {enemy.name} for {damage}")
        enemy.change_health(-(damage))

    def use_item(self, current_enemy):

        for key, value in self.inv.items():
            print(f"{key}: {value}")

        print("\nWhich Item would you like to use?")
        response = input()
        for key in self.inv:
            if response.lower() == key:
                match key:
                    case "food":
                        self.change_health(30)
                    case "water":
                        self.current_mp += 20
                    case "donut":
                        if current_enemy.name == 'Fat Cop':
                            print(f"\nItem Used: {key}")
                            print(self.inv[key])
                            return "end"
                    case "emp":
                        if current_enemy.name == 'Robot Clone' or current_enemy.name == 'Motorcycle Tank':
                            print(f"\nItem Used: {key}")
                            print(self.inv[key])
                            return "end"
                    case "smelly spray":
                        if current_enemy.name == 'Gross Bug' or current_enemy.name == 'Large Rat' or current_enemy.name == 'Rabid Dog' or current_enemy.name == 'Mysterious Chimpanzee' or current_enemy.name == 'Huge Bear':
                            print(f"\nItem Used: {key}")
                            print(self.inv[key])
                            return "end"
                    case "blank check":
                        if current_enemy.name == 'Corperate Goon' or current_enemy.name == 'Paid Professional' or current_enemy.name == 'Corrupt Executive':
                            print(f"\nItem Used: {key}")
                            print(self.inv[key])
                            return "end"
                    case "gun":
                        self.current_atk = self.max_atk
                    case "book":
                        self.base_atk += 1
                        self.base_dfs += 1
                        self.base_hp += 1
                        self.base_mp += 1
                    case "energy drink":
                        self.base_spd += 1
                        self.change_health(-5)
                    case _:
                        print("That's not a valid item!")

                print(f"\nItem Used: {key}")
                print(self.inv[key])

        self.inv.pop(response.lower())

    def level_up(self):
        print("You've leveled up!")
        print("HP + 5")
        print("MP + 5")
        print("ATTACK + 1")
        print("DEFENSE + 1")
        print("SPEED + 1")

        self.base_hp += 5
        self.base_mp += 5
        self.base_atk += 1
        self.base_dfs += 1
        self.base_spd += 1

    def die(self):
        print("""
        
    YOU HAVE DIED!
    It's a tough world out there and you weren't able to make it. 
    Now your bones litter the wayside and your existence is slowly forgotten.
    Perhaps if things were different, and you were in another time or place.
    If you wish your soul may try again.
        
        """)
        if input():                                                             # TODO: Go back to main menu instead of exiting
            sys.exit()
        

