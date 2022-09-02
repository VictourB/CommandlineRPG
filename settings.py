spoils_DSC = {
    "food" : "Food heals 30 HP.",
    "water" : "Water recovers 20 MP.",
    "donut" : "this Donut will end any encounter with a cop.",
    "emp" : "This device will end any encounter with a machine.",
    "smelly spray" : "This will end any encounter with an animal.",
    "blank check" : "This will end any encounter with people in suits.",
    "gun" : "This item will max out your Attack.",
    "book" : "Permanent +1 to HP, MP, Attack, and Defense.",
    "energy drink" : "Permanent +1 to Speed and -5 to HP."
}

moxie_moves_DSC = {
    "Papercut" : "The next attack will hit twice.",
    "Gross Out" : "Grossed out people can't use items at all!",
    "Big Bite" : "This attack will slow the opponent to a standstill for two turns.",
    "Possession" : "The opponent's Moxie Points will degrade by 5 every turn.",
    "Rabies" : "The opponent's Health Points will degrade by 5 every turn.",
    "Beatdown" : "The opponent will takes 10 points of damage and lose their next turn",
    "Liquid Rage" : "This will raise Attack by 5 points.",
    "Lord's Protection" : "This will raise Defense by 5 points.",
    "Deadly Weapon" : "This move will max out Speed for three turns.",
    "Mind Games" : "Reduces opponent's Defense to 0.",
    "Corperate Ladder" : "A literal ladder that will hit for 3x the amount of damage.",
    "Deafening Roar" : "Summons an ally to help in the fight.",
    "Done Deed" : "Reduces HP to 10, Reduces opponents Defense, Speed and MP to 0",
    "Unlimited Funding" : "Heal 10 HP every turn.",
    "Electric Sheep" : "A bomb fashioned after a sheep, explodes for 5x damage but has a 25\% chance of being a dud",
    "Obelisk" : "Raises Attack, Defense and Speed by 2. Raises MP and HP by 10.",
    "Abduction" : "The opponent loses their next 2 turns and MP is reduced to 0",
    "Polarized Hull" : "This move will max out every stat except MP."
}


# HP 1 (nearly dies on it's own) - 100 (Virtually unkillable)
# MP 0 (No Magic) - 80 (unlimited power)
# ATK 1 (pinch) - 20 (debilitating injury)
# DEF 1 (unarmored skin) - 20 (Completely Armoured)
# SPEED 0 (immobile) - 10 (quicker than The Flash)

EASY_ENCOUNTERS = {
    'Tall Grass' : {'HP' : 5, 'MP' : 0, 'ATK' : 1, "DEF" : 0, "SPEED" : 0, "DSC" : "It's just some tall grass that could be easily cut down.", "MM" : "Papercut"},
    'Gross Bug' : {'HP' : 10, 'MP' : 0, 'ATK' : 2, "DEF" : 1, "SPEED" : 1, "DSC" : "Ewww, it's a gross looking bug with lots of legs and a fat head.", "MM" : "Gross Out"  },
    'Large Rat' : {'HP' : 20, 'MP' : 0, 'ATK' : 3, "DEF" : 2, "SPEED" : 2, "DSC" : "WOW! It's one of the biggest rats you've ever seen.", "MM" : "Big Bite"  },
    'Spooky Ghost' : {'HP' : 30, 'MP' : 5, 'ATK' : 5, "DEF" : 5, "SPEED" : 3, "DSC" : "It's a ghost, an actual ghost, you can hardly believe it!", "MM" : "Possession"  },
    'Rabid Dog' : {'HP' : 30, 'MP' : 10, 'ATK' : 6, "DEF" : 7, "SPEED" : 4, "DSC" : "It's a large agitated dog, and you can see foam dripping from it's mouth.", "MM" : "Rabies"  }  
}

ITERMEDIATE_ENCOUNTERS = {
    '14 Year Old' : {'HP' : 40, 'MP' : 15, 'ATK' : 7, "DEF" : 8, "SPEED" : 6, "DSC" : "There's a kid getting off their bicycle. They have a baseball bat for some reason.", "MM" : "Beatdown"  },
    'Local Drunk' : {'HP' : 50, 'MP' : 20, 'ATK' : 8, "DEF" : 9, "SPEED" : 4, "DSC" : "Their breath stinks and they can barely walk. It's the local drunk.", "MM" : "Liquid Rage"  },
    'Insistant Missionary' : {'HP' : 45, 'MP' : 40, 'ATK' : 5, "DEF" : 11, "SPEED" : 6, "DSC" : "This missonary won't take no for an answer and plans to send you to God.", "MM" : "Lord's Protection"  },
    'Fat Cop' : {'HP' : 60, 'MP' : 30, 'ATK' : 10, "DEF" : 13, "SPEED" : 4, "DSC" : "They have a baton but can barely walk.", "MM" : "Deadly Weapon"  },
    'Cool Cultist' : {'HP' : 50, 'MP' : 45, 'ATK' : 8, "DEF" : 7, "SPEED" : 6, "DSC" : "This cultist is a super cool person but still believes in wacko stuff.", "MM" : "Mind Games"  }  
}

DIFFICULT_ENCOUNTERS = {
    'Corperate Goon' : {'HP' : 60, 'MP' : 60, 'ATK' : 9, "DEF" : 10, "SPEED" : 7, "DSC" : "This goon hopes that defeating you will lead to that much need promotion.", "MM" : "Corperate Ladder"  },
    'Huge Bear' : {'HP' : 80, 'MP' : 40, 'ATK' : 14, "DEF" : 8, "SPEED" : 8, "DSC" : "This grizzly bear is enormous and is growling agressively.", "MM" : "Deafening Roar"  },
    'Paid Professional' : {'HP' : 70, 'MP' : 65, 'ATK' : 12, "DEF" : 14, "SPEED" : 7, "DSC" : "You are just another job for this professional contract killer.", "MM" : "Done Deed"  },
    'Corrupt Executive' : {'HP' : 70, 'MP' : 65, 'ATK' : 12, "DEF" : 12, "SPEED" : 7, "DSC" : "Affecting this executive's profits was a mistake. One you won't make again.", "MM" : "Unlimited Funding"  },
    'Robot Clone' : {'HP' : 90, 'MP' : 70, 'ATK' : 18, "DEF" : 18, "SPEED" : 9, "DSC" : "They have studied you and created a replica that will wipe you out. ", "MM" : "Electric Sheep"  }  
}

EASY_BOSS = {'Mysterious Chimpanzee' : {'HP' : 30, 'MP' : 20, 'ATK' : 7, "DEF" : 7, "SPEED" : 5, "DSC" : "It's a monkey, upon closer inspection there's something strange about it.", "MM" : "Obelisk"  }}

INTERMEDIATE_BOSS = {'Violent Psychopath' : {'HP' : 70, 'MP' : 40, 'ATK' : 14, "DEF" : 14, "SPEED" : 8, "DSC" : "They're not messing around. Murder is the only goal for this freak.", "MM" : "Abduction" }}

DIFFICULT_BOSS = {'Motorcycle Tank' : {'HP' : 100, 'MP' : 60, 'ATK' : 20, "DEF" : 20, "SPEED" : 10, "DSC" : "Fast like a bike and indestructable like a tank. The machine barreling towards you will show no mercy.", "MM" : "Polarized Hull"  }}
