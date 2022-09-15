import sys, random
from entity import Entity
import settings


class Player(Entity):
    def __init__(self, name,description,hp,mp,atk,dfs,spd) -> None:
        super().__init__(name,description,hp,mp,atk,dfs,spd)
        self.inv = settings.spoils_DSC
        self.mm = {}
        # self.mm = settings.moxie_moves_DSC

    def attack(self, enemy):
        damage = self.current_atk - enemy.current_dfs
        if damage < 0:
            damage = 0
        print(f"\n{self.name} attacked {enemy.name} for {damage}")
        enemy.change_health(-(damage))

    def use_item(self, current_enemy):
        effect = None
        for key, value in self.inv.items():
            print(f"{key}: {value}")

        print("\nWhich Item would you like to use?")
        response = input()
        if response.lower() not in self.inv:
            print("That's not a valid item!")
            return
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
                            effect = "end"
                    case "emp":
                        if current_enemy.name == 'Robot Clone' or current_enemy.name == 'Motorcycle Tank':
                            print(f"\nItem Used: {key}")
                            print(self.inv[key])
                            effect = "end"
                    case "smelly spray":
                        if current_enemy.name == 'Gross Bug' or current_enemy.name == 'Large Rat' or current_enemy.name == 'Rabid Dog' or current_enemy.name == 'Mysterious Chimpanzee' or current_enemy.name == 'Huge Bear':
                            print(f"\nItem Used: {key}")
                            print(self.inv[key])
                            effect = "end"
                    case "blank check":
                        if current_enemy.name == 'Corperate Goon' or current_enemy.name == 'Paid Professional' or current_enemy.name == 'Corrupt Executive':
                            print(f"\nItem Used: {key}")
                            print(self.inv[key])
                            effect = "end"
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
        return effect

    def use_moxie(self):
        effect = None

        for key, value in self.mm.items():
            print(f"{key}: {value}")

        print("\nWhich MM would you like to use?")
        response = input()
        if response.title() not in self.mm:
            print("That is not a valid Moxie Move")
            return
        for key in self.mm:
            if response.title() == key:
                self.currrent_mm = response.title()
                if self.currrent_mm == "Papercut":            # The next attack will hit twice.
                    effect = "2x"
                elif self.currrent_mm == "Gross Out":         # Grossed out people can't use items at all!
                    pass
                elif self.currrent_mm == "Big Bite":          # This attack will slow the opponent to a standstill for two turns.
                    pass
                elif self.currrent_mm == "Possession":        # The opponent's Moxie Points will degrade by 5 every turn.
                    pass
                elif self.currrent_mm == "Rabies":            # The opponent's Health Points will degrade by 5 every turn.
                    pass
                elif self.currrent_mm == "Beatdown":          # The opponent will takes 10 points of damage and lose their next turn
                    pass
                elif self.currrent_mm == "Liquid Rage":       # This will raise Attack by 5 points.
                    pass
                elif self.currrent_mm == "Lord's Protection": # This will raise Defense by 5 points.
                    pass
                elif self.currrent_mm == "Deadly Weapon":     # This move will max out Speed for three turns.
                    pass
                elif self.currrent_mm == "Mind Games":        # Reduces opponent's Defense to 0
                    pass
                elif self.currrent_mm == "Corperate Ladder":  # A literal ladder that will hit for 3x the amount of damage.
                    pass
                elif self.currrent_mm == "Deafening Roar":    # Summons an ally to help in the fight.
                    pass
                elif self.currrent_mm == "Done Deed":         # Reduces HP to 10, Reduces opponents Defense, Speed and MP to 0
                    pass
                elif self.currrent_mm == "Unlimited Funding": # Heal 10 HP every turn.        
                    pass
                elif self.currrent_mm == "Electric Sheep":    # A bomb fashioned after a sheep, explodes for 5x damage but has a 25% chance of being a dud
                    pass
                elif self.currrent_mm == "Obelisk":           # Raises Attack, Defense and Speed by 2. Raises MP and HP by 10.
                    pass
                elif self.currrent_mm == "Abduction":         # The opponent loses their next 2 turns and MP is reduced to 0
                    pass
                elif self.currrent_mm == "Polarized Hull":    # This move will max out every stat except MP.
                    pass
                else:
                    print("That is not a valid command")
                    return

                print(f"\n{self.name} Used: {key}")
                print(self.mm[key])
            
        self.current_mp -= 5
        return effect

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
        input()                                                             # TODO: Go back to main menu instead of exiting
        sys.exit()
        

