#! python3
# Command Line RPG - Can you make it to the end and fight the boss?
# By Victour Bue

from random import random
from player import Player
import settings
import math
import random
import entity

def prompt():
    print()
    print("Would you like to play a jaw-dropping RPG with twists and turn around every corner?")
    response = input("Yes/No \n")
    if response.lower() == "yes":
        return
    elif response.lower() == "no":
        return False
    else:
        print("Sorry, but I don't understand that.")
        return prompt()

def create_character():
    hp = 10
    mp = 10
    atk = 1
    dfs = 1
    spd = 1

    print()
    print("CREATING CHARACTER")
    name = input("What is your character's name? ")
    while True:
        description = input("Please enter a short description for you character. ")
        if len(description) > 80:
            print("That description is too long, please enter something 80 characters or less. ")
        elif len(description) < 3:
            print("That description is too short, please enter something 3 characters or more. ")
        else:
            break
    print()
    print("Please give your character 3 stats")
    for stat in range(3):
        print(stat)
        response = input("Would you like to increase (H)it Points, (M)oxie Points, (A)ttack, (D)efense, or (S)peed? ")
        if response.lower() == "hit points" or response.lower() == "h":
            print("+5 HP")
            hp += 5
        elif response.lower() == "moxie points" or response.lower() == 'm':
            print("+5 Moxie Points")
            mp += 5
        elif response.lower() == "attack" or response.lower() == "a":
            print("+1 Attack")
            atk += 1
        elif response.lower() == "defense" or response.lower() == "d":
            print("+1 Defense")
            dfs += 1
        elif response.lower() == "speed" or response.lower() == "s":
            print("+1 Speed")
            spd += 1
        else:
            print("Sorry I don't understand that.")
            stat -= 1
    
    while True:
        print("So you want this character:")

        # This part is exists in player class but is needed before player exists.
        print(f"""
        
        {name.capitalize()}
        {description}

        Hit Points: {hp}
        Moxie Points: {mp}
        Attack: {atk}
        Defense {dfs}
        speed: {spd}
        
        """)

        confirm = input("Yes/No \n")
        if confirm.lower() == "yes":
            player = Player(name, description, hp, mp, atk, dfs, spd)
            print("Character Created!")
            return player
        elif confirm.lower() == "no":
            return create_character()
        else:
            print("I didn't understand that")

def encounter(player, story_beat):

    if story_beat == 0:
        encounter_difficulty = settings.EASY_ENCOUNTERS
    if story_beat == 1:
        encounter_difficulty = settings.EASY_BOSS
    if story_beat == 2:
        encounter_difficulty = settings.ITERMEDIATE_ENCOUNTERS
    if story_beat == 3:
        encounter_difficulty = settings.INTERMEDIATE_BOSS
    if story_beat == 4:
        encounter_difficulty = settings.DIFFICULT_ENCOUNTERS
    if story_beat == 5:
        encounter_difficulty = settings.DIFFICULT_BOSS


    for round in encounter_difficulty:                                                   # Round Loop
        enemy_info = encounter_difficulty[round]

        current_enemy = entity.Enemy(round, enemy_info['DSC'], enemy_info['HP'], enemy_info['MP'], enemy_info['ATK'], enemy_info['DEF'], enemy_info['SPEED'],enemy_info['MM'])
        while current_enemy.current_hp > 0:                                                 # Turn Loop While Enemy Alive
            turn_number = 0        
            current_enemy.describe()

            print("What would you like to do?")
            action = input("(A)ttack | (D)efend | (M)oxie | (I)nventory | (S)tatus | (R)un \n\n")
            print()
            match action.lower():
                case "attack":
                    print("Attacking!")
                    current_enemy.change_health(-(player.current_atk))
                case "a":
                    print("Attacking!")
                    current_enemy.change_health(-(player.current_atk))
                case "defend":
                    print("Defending!")
                    player.defend()
                case "d":
                    print("Defending!")
                    player.defend()
                case "moxie":
                    print("Using Moxie!")
                    player.use_moxie()
                case "m":
                    print("Using Moxie!")
                    player.use_moxie()
                case "inventory":
                    print("Opening Inventory!")
                    player.use_item()
                case "i":
                    print("Opening Inventory!")
                    player.use_item()
                case "status":
                    print("Getting Status!")
                    player.describe()
                case "s":
                    print("Getting Status!")
                    player.describe()
                case "run":
                    print("Attempting to Run!")
                    chance_to_escape = (player.current_spd * 5) / 100
                    chance_to_escape_and_heal = (player.current_spd * 2) / 100
                    roll = random.random()
                    if roll <= chance_to_escape_and_heal:
                        print(f"you got {roll} and was able to escape and heal a bit")
                        break
                    elif roll <= chance_to_escape:
                        print(f"you got {roll} and was able to escape")
                        break
                case "r":
                    print("Attempting to Run!")
                    chance_to_escape = (player.current_spd * 5) / 100
                    chance_to_escape_and_heal = (player.current_spd * 2) / 100
                    roll = random.random()
                    if roll <= chance_to_escape_and_heal:
                        print(f"you got {roll} and was able to escape and heal a bit")
                        break
                    elif roll <= chance_to_escape:
                        print(f"you got {roll} and was able to escape")
                        break
                case _:
                    print("That's not a valid command.")
                    pass

            current_enemy.debuff(turn_number)
            player.debuff(turn_number)
            turn_number += 1


def story(story_beat):
    if story_beat == 0:
        print("""
        
        This story starts when you awoke one day to find your family killed,
        and a mysterious note detailing a plan to turn the world into robot consumers.

        You venture out of the homestead hoping to avenge your family and sabotoge the evil plan to roboticize the world.
        
        """)
        pass # Easy Enemies

    if story_beat == 1:
        print("""
        
        After destroying many foes, you take a while to bask in the glory of victory, but wait!
        Across from the trees comes a loud screaking oponent that might just give you more trouble then you can handle.

        Watch out and try to get out of it alive.
        
        """)
        pass # Easy Boss
    if story_beat == 2:
        print("""
        
        Wow that was a tough character, but now you can see glimpses of civilization. The hussle and bussle,
        the flow of people and traffic. Not to mention the nonstop gossip!

        You decide to check out local robotic and industrial areas. 
        
        """)

        pass # Medium Enemies
    if story_beat == 3:
        print("""
        
        After getting through the city alive you stop in an alleyway to catch your breath.
        There are so many shifty people around here that you start to fear for your life.

        Why did you go on this stupid crusade? you're just gonna end up dead like the rest of your family.
        You pass out in the pool of rain, piss and self pity.

        When you wake up you're not in an alley anymore!
        It's dark but you see someone in the corner.
        
        """)
        pass # Medium Boss
    if story_beat == 4:
        print("""
        
        In a series of lucky breaks you are back on the case, 
        it seems as though the true villian, the one who killed your loved ones is none other than
        Jason Bleak international entrepaneur extrodinare. 

        Unknown to the public Jason has a severe pychotic tendency and often makes violent accusasions.
        It seems as though one day he saw your homestead on a map and became fixated on the idea
        that you were secretly blocking his sub-sonic information relay system (SSIRS).
        Causing him to accumulate money slightly less rapidly.

        Since he is so rich nobody stops him from doing whatever he wants and goes through greats stakes
        to cover up his crimes. 

        In fact, he has grown aware of you and already fled the country. You'll probably never see him again.
        He has sent his entire aresenal of wealth to destory you.

        The only hope is to destroy the Robot Production Facility.
        
        """)    
        pass # Difficult Enemies
    if story_beat == 5:
        print("""
        
        From the ashes of the burn down factory emerges an enemy so powerful, so deadly, so vicious
        you could be forgiven for thinking it was satan himself.

        No simple man could survive this!
        
        """)
        pass # Difficult Boss













def main():
    if prompt() == False: return
    player = create_character()
    story_beat = 0
    while True:
        story(story_beat)
        encounter(player, story_beat)
        story_beat += 1
        if story_beat >= 6 or player.current_hp <= 0:
            break
    
    
main()

