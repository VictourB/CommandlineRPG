
import settings

class Entity():
    def __init__(self, name,description,hp,mp,atk,dfs,spd) -> None:

        self.name = name
        self.description = description
 
        self.base_hp = hp
        self.current_hp = hp
        self.max_mp = mp
        self.base_mp = mp
        self.current_mp = mp
        self.max_atk = atk
        self.base_atk = atk
        self.current_atk = atk
        self.max_dfs = dfs
        self.base_dfs = dfs
        self.current_dfs = dfs
        self.max_spd = spd
        self.base_spd = spd
        self.current_spd = spd

        self.inv = {}

        self.mm = settings.moxie_moves_DSC
        self.current_mm = ""
    
    def describe(self):
        print(f"""
        
        {self.name}
        {self.description}

        Hit Points: {self.current_hp} / {self.base_hp}
        Moxie Points: {self.current_mp} / {self.base_mp}
        Attack: {self.current_atk} / {self.base_atk}
        Defense {self.current_dfs} / {self.base_dfs}
        Speed: {self.current_spd} / {self.base_spd}
        
        """)
    
    def defend(self):
        self.current_dfs += int(self.base_dfs)

    def use_moxie(self):
        effect = None

        if self.current_mm == "Papercut":            # The next attack will hit twice.
            effect = "2x"
        elif self.current_mm == "Gross Out":         # Grossed out people can't use items at all!
            pass
        elif self.current_mm == "Big Bite":          # This attack will slow the opponent to a standstill for two turns.
            pass
        elif self.current_mm == "Possession":        # The opponent's Moxie Points will degrade by 5 every turn.
            pass
        elif self.current_mm == "Rabies":            # The opponent's Health Points will degrade by 5 every turn.
            pass
        elif self.current_mm == "Beatdown":          # The opponent will takes 10 points of damage and lose their next turn
            pass
        elif self.current_mm == "Liquid Rage":       # This will raise Attack by 5 points.
            pass
        elif self.current_mm == "Lord's Protection": # This will raise Defense by 5 points.
            pass
        elif self.current_mm == "Deadly Weapon":     # This move will max out Speed for three turns.
            pass
        elif self.current_mm == "Mind Games":        # Reduces opponent's Defense to 0
            pass
        elif self.current_mm == "Corperate Ladder":  # A literal ladder that will hit for 3x the amount of damage.
            pass
        elif self.current_mm == "Deafening Roar":    # Summons an ally to help in the fight.
            pass
        elif self.current_mm == "Done Deed":         # Reduces HP to 10, Reduces opponents Defense, Speed and MP to 0
            pass
        elif self.current_mm == "Unlimited Funding": # Heal 10 HP every turn.        
            pass
        elif self.current_mm == "Electric Sheep":    # A bomb fashioned after a sheep, explodes for 5x damage but has a 25% chance of being a dud
            pass
        elif self.current_mm == "Obelisk":           # Raises Attack, Defense and Speed by 2. Raises MP and HP by 10.
            pass
        elif self.current_mm == "Abduction":         # The opponent loses their next 2 turns and MP is reduced to 0
            pass
        elif self.current_mm == "Polarized Hull":    # This move will max out every stat except MP.
            pass
        else:
            print("That is not a valid command")
            return self.use_moxie()


        print(f"\n{self.name} Used: {self.current_mm}")
        print(self.mm[self.current_mm])

        self.current_mp -= 5
        return effect










        
    
    def debuff(self, turn_number):

        if abs(self.current_hp - self.base_hp) < 1:
            self.current_hp = self.base_hp
        else:
            if self.current_hp > self.base_hp:
                self.current_hp -= 1
            elif self.current_hp < self.base_hp:
                self.current_hp += 1

        if abs(self.current_mp - self.base_mp) < 1:
            self.current_mp = self.base_mp
        else:
            if self.current_mp > self.base_mp:
                self.current_mp -= 1
            elif self.current_mp < self.base_mp:
                self.current_mp += 1
        
        if self.current_atk > self.base_atk:
            self.current_atk -= 1
        elif self.current_atk < self.base_atk:
            self.current_atk += 1
        
        if self.current_dfs > self.base_dfs:
            self.current_dfs -= 1
        elif self.current_dfs < self.base_dfs:
            self.current_dfs += 1

        if self.current_spd > self.base_spd:
            self.current_spd -= 1
        elif self.current_spd < self.base_spd:
            self.current_spd += 1
    
    def die(self):
        pass

    def change_health(self, health_int):
        self.current_hp += health_int 
        self.base_hp += int(health_int * .2)
        if self.current_hp <= 0:
            self.die()



class Enemy(Entity):
    def __init__(self, name, description, hp, mp, atk, dfs, spd, mm) -> None:
        super().__init__(name, description, hp, mp, atk, dfs, spd)
        self.current_mm = mm

    def attack(self, player):
        damage = self.current_atk - player.current_dfs
        if damage < 0:
            damage = 0
        print(f"\n{self.name} attacked {player.name} for {damage}")
        player.change_health(-(damage))

    