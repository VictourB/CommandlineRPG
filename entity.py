
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

        self.mm = []
        self.currrent_mm = ""
    
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
        pass
    
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
        self.mm = mm

    def attack(self, player):
        damage = self.current_atk - player.current_dfs
        if damage < 0:
            damage = 0
        print(f"\n{self.name} attacked {player.name} for {damage}")
        player.change_health(-(damage))

    