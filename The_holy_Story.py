import random
import json
elements = ["Fire", "Ice", "Lightning", "Earth", "Water", "Air", "Darkness", "Light", "Poison", "Chaos"]

all_mobs = {
    "Goblin of Darkness": {"health": 50, "damage": 10, "element": "Darkness"},
    "Shadow Orc": {"health": 100, "damage": 20, "element": "Darkness"},
    "Eclipse Dragon": {"health": 200, "damage": 30, "element": "Darkness"},
    "Nightmare Zombie": {"health": 60, "damage": 12, "element": "Darkness"},
    "Dark Skeleton": {"health": 75, "damage": 15, "element": "Darkness"},
    "Cave Troll": {"health": 90, "damage": 18, "element": "Darkness"},
    "Venomous Spider": {"health": 80, "damage": 14, "element": "Poison"},
    "Witch of Shadows": {"health": 70, "damage": 16, "element": "Darkness"},
    "Vampire Lord": {"health": 120, "damage": 25, "element": "Darkness"},
    "Shadow Lich": {"health": 150, "damage": 28, "element": "Darkness"},
    "Dark Golem": {"health": 180, "damage": 20, "element": "Darkness"},
    "Imp of Chaos": {"health": 40, "damage": 8, "element": "Chaos"},
    "Banshee Wail": {"health": 60, "damage": 14, "element": "Darkness"},
    "Griffin of the Night": {"health": 100, "damage": 22, "element": "Darkness"},
    "Gorgon of Shadows": {"health": 110, "damage": 24, "element": "Darkness"},
    "Harpy Screamer": {"health": 70, "damage": 15, "element": "Darkness"},
    "Hydra of the Abyss": {"health": 200, "damage": 30, "element": "Darkness"},
    "Manticore of the Deep": {"health": 130, "damage": 25, "element": "Darkness"},
    "Minotaur of the Labyrinth": {"health": 140, "damage": 28, "element": "Darkness"},
    "Mummy of the Tomb": {"health": 90, "damage": 20, "element": "Darkness"},
    "Phoenix of Darkness": {"health": 160, "damage": 30, "element": "Darkness"},
    "Rat King": {"health": 30, "damage": 6, "element": "Poison"},
    "Djinn of Shadows": {"health": 80, "damage": 18, "element": "Darkness"},
    "Kraken of the Depths": {"health": 200, "damage": 35, "element": "Darkness"},
    "Wraith of the Night": {"health": 70, "damage": 15, "element": "Darkness"},
    "Behemoth of the Earth": {"health": 250, "damage": 35, "element": "Earth"},
    "Cyclops of the Mountains": {"health": 120, "damage": 22, "element": "Earth"},
    "Wyvern of the Skies": {"health": 140, "damage": 28, "element": "Air"},
    "Naga of the Seas": {"health": 110, "damage": 20, "element": "Water"},
    "Lamia of the Abyss": {"health": 80, "damage": 18, "element": "Darkness"},
    "Dark Knight": {"health": 200, "damage": 30, "element": "Darkness"},
    "Frost Giant": {"health": 200, "damage": 35, "element": "Ice"},
    "Fire Elemental": {"health": 150, "damage": 25, "element": "Fire"},
    "Earth Elemental": {"health": 160, "damage": 28, "element": "Earth"},
    "Water Elemental": {"health": 150, "damage": 22, "element": "Water"},
    "Air Elemental": {"health": 140, "damage": 20, "element": "Air"},
    "Shade": {"health": 80, "damage": 16, "element": "Darkness"},
    "Ghoul": {"health": 90, "damage": 18, "element": "Darkness"},
    "Hellhound": {"health": 120, "damage": 24, "element": "Fire"},
    "Basilisk": {"health": 100, "damage": 20, "element": "Earth"},
    "Reaper": {"health": 130, "damage": 28, "element": "Darkness"},
    "Dire Wolf": {"health": 70, "damage": 14, "element": "Earth"},
    "Shadow Fiend": {"health": 90, "damage": 20, "element": "Darkness"},
    "Roc": {"health": 150, "damage": 30, "element": "Air"},
    "Storm Dragon": {"health": 220, "damage": 35, "element": "Lightning"},
    "Death Knight": {"health": 180, "damage": 30, "element": "Darkness"},
    "Elder Dragon": {"health": 250, "damage": 40, "element": "Darkness"},
    "Ancient Golem": {"health": 250, "damage": 35, "element": "Earth"},
    "Specter": {"health": 70, "damage": 15, "element": "Darkness"},
    "Dreadlord": {"health": 160, "damage": 30, "element": "Darkness"},
    "Chaos Beast": {"health": 180, "damage": 35, "element": "Chaos"},
    "Nightmare": {"health": 90, "damage": 20, "element": "Darkness"},
    "Celestial Being": {"health": 250, "damage": 40, "element": "Light"}
}

antagonists = [
    {
        "name": "Lord Nox",
        "description": "A powerful sorcerer who seeks to plunge the world into eternal darkness.",
        "level_requirement": 10
    },
    {
        "name": "Queen Seraphina",
        "description": "A fallen angel with dominion over fire, seeking to burn the world to ashes.",
        "level_requirement": 20
    },
    {
        "name": "Kraken King",
        "description": "A monstrous sea creature that controls the oceans and devours ships whole.",
        "level_requirement": 30
    },
    {
        "name": "Necromancer Zul",
        "description": "A necromancer who raises the dead to do his bidding, seeking to rule the world with an undead army.",
        "level_requirement": 40
    },
    {
        "name": "Void Warden",
        "description": "A being from another dimension, aiming to engulf the world in eternal chaos.",
        "level_requirement": 50
    }
]

islands = [
    {"name": "Forest", "description": "A land filled with magical creatures and mysterious temples.", "level_requirement": 1, "has_village": True, "has_temple": True},
    {"name": "Dungen", "description": "A hole in a cave with monsters all over it that rose to the top.", "level_requirement": 20, "has_village": True, "has_temple": True},
    {"name": "Mystic Island", "description": "A land filled with magical creatures and mysterious temples.", "level_requirement": 1, "has_village": True, "has_temple": True},
    {"name": "Frost Island", "description": "An icy landscape inhabited by frost giants, with an ancient temple.", "level_requirement": 5, "has_village": True, "has_temple": True},
    {"name": "Volcano Island", "description": "A fiery terrain with lava pits and a temple of the Fire God.", "level_requirement": 10, "has_village": False, "has_temple": True},
    {"name": "Shadow Island", "description": "A dark and eerie place, rumored to be the lair of Lord Nox.", "level_requirement": 15, "has_village": False, "has_temple": False}
]

for i in range(6, 103):
    islands.append({
        "name": f"Island {i}",
        "description": f"A mysterious island filled with adventures and dangers. Explore at your own risk.",
        "level_requirement": i,
        "has_village": random.choice([True, False]),
        "has_temple": random.choice([True, False])
    })

subclasses = {
    "Warrior": [
        "Radiant Knight", "Sun Crusader", "Celestial Guardian", "Luminous Vanguard", "Dawn Bringer", "Light Champion",
        "Solar Paladin", "Shining Sentinel", "Glory Warrior", "Aurora Knight", "Holy Defender", "Seraphic Warrior",
        "Illuminated Guardian", "Lightbearer", "Divine Protector", "Sunblade", "Golden Knight", "Radiant Defender",
        "Lightbringer", "Heavenly Sentinel", "Beacon Knight", "Daylight Warrior", "Seraphic Paladin", "Aether Knight",
        "Luminescent Warrior", "Solar Protector", "Celestial Vanguard", "Skyward Sentinel", "Light's Champion", "Brilliant Guardian",
        "Dawnbreaker", "Sunshine Warrior", "Radiant Sentry", "Blazing Knight", "Gleaming Guardian", "Luminous Knight",
        "Light's Defender", "Golden Paladin", "Heaven's Blade", "Illuminator", "Star Guardian", "Sky Sentinel"
    ],
    "Archer": [
        "Sun Archer", "Luminous Marksman", "Celestial Sniper", "Radiant Ranger", "Golden Bowman", "Aurora Scout",
        "Sunstriker", "Lightpath Archer", "Skyward Hunter", "Gleaming Sharpshooter", "Daylight Bowmaster", "Radiant Stalker",
        "Luminous Tracker", "Solar Archer", "Heavenly Bowman", "Starfall Ranger", "Lightbound Archer", "Dawn's Eye",
        "Sunflare Sniper", "Beacon Bowman", "Illuminated Hunter", "Glory Seeker", "Sky Archer", "Radiant Bowmaster",
        "Sunlit Ranger", "Sunbeam Sniper", "Light Sentinel", "Celestial Huntsman", "Star Archer", "Light's Arrow",
        "Radiant Scout", "Dawnstrider", "Shining Marksman", "Glowing Archer", "Sunlit Sharpshooter", "Golden Arrow",
        "Heaven's Marksman", "Sky Hunter", "Starlight Archer", "Gleaming Bowmaster", "Luminous Sentinel", "Solar Hunter"
    ],
    "Mage": [
        "Light Sorcerer", "Sun Wizard", "Celestial Mage", "Radiant Enchanter", "Luminous Sage", "Sunbeam Conjurer",
        "Aurora Mage", "Illuminator", "Gleaming Warlock", "Daylight Sorcerer", "Sunflare Magician", "Beacon Caster",
        "Lightbringer Mage", "Heavenly Sage", "Starfall Wizard", "Glory Magus", "Luminescent Spellcaster", "Celestial Archmage",
        "Dawn Enchanter", "Sunburst Wizard", "Radiant Illusionist", "Illuminated Seer", "Sky Mage", "Light Weaver",
        "Luminous Conjurer", "Dawncaster", "Radiant Elementalist", "Light Sage", "Sunlight Sorcerer", "Skyward Magician",
        "Heavenly Wizard", "Starlight Enchanter", "Gleaming Conjurer", "Luminous Magus", "Celestial Sorcerer", "Radiant Sage",
        "Beacon of Light", "Shining Wizard", "Light Archmage", "Aurora Caster", "Golden Enchanter", "Illuminated Mystic"
    ]
}

all_weapons = {
    "Warrior": [
        "Short Sword", "Long Sword", "Great Sword", "Hand Axe", "Battle Axe", "War Axe", "Wooden Mace", "Iron Mace", "Spiked Mace", "Spear",
        "Broadsword", "Claymore", "Warhammer", "Halberd", "Battle Hammer", "Maul", "Glaive", "Pike", "Polearm", "Morning Star",
        "Scimitar", "Kris", "Crescent Blade", "Cutlass", "Bastard Sword", "Flail", "Hand Axe", "Throwing Axe", "Light Mace", "Heavy Mace",
        "War Club", "Greataxe", "Dire Sword", "Dragon Mace", "Heavy Warhammer", "Viking Axe", "Champion's Sword", "Giant's Club", "Stormhammer", "Colossal Axe"
    ],
    "Archer": [
        "Short Bow", "Long Bow", "Crossbow", "Recurve Bow", "Compound Bow", "Longbow", "Blowgun", "Light Crossbow", "Heavy Crossbow", "Composite Bow",
        "War Bow", "Hunting Bow", "Elven Bow", "Magic Bow", "Flaming Bow", "Ice Bow", "Lightning Bow", "Storm Bow", "Shadow Bow", "Silent Bow",
        "Swift Bow", "Ancient Bow", "Ranger's Bow", "Sniper's Bow", "Falcon Bow", "Eagle's Bow", "Celestial Bow", "Tranquil Bow", "Hunter's Crossbow",
        "Wind Bow", "Dragon's Crossbow", "Silver Bow", "Golden Bow", "Emerald Bow", "Elven Longbow", "Hunter's Recurve Bow", "Phantom Bow", "Cursed Bow"
    ],
    "Mage": [
        "Wooden Staff", "Iron Staff", "Mystic Staff", "Fire Staff", "Ice Staff", "Lightning Staff", "Arcane Staff", "Eldritch Staff", "Dark Staff", "Healing Staff",
        "Sorcerer's Staff", "Elemental Staff", "Wizard's Staff", "Enchanter's Rod", "Mystic Wand", "Crystal Rod", "Staff of Power", "Rune Staff", "Celestial Wand", "Arcane Rod",
        "Staff of Wisdom", "Staff of Flames", "Frost Rod", "Staff of Light", "Shadow Wand", "Necromancer's Staff", "Staff of the Elements", "Eldritch Wand", "Celestial Staff", "Wand of Healing",
        "Fire Wand", "Ice Wand", "Lightning Wand", "Staff of the Ancients", "Staff of the Mages", "Ethereal Staff", "Staff of Knowledge", "Wizard's Wand", "Enchanter's Wand", "Staff of Shadows"
    ]
}

base_weapons = {
    "Warrior": [
        "Dragon Slayer Sword", "Excalibur", "Mjolnir", "Giant's Axe", "Meteor Hammer", "Celestial Mace", "Frostbrand Sword", "Flaming Great Sword", "Shadow Warhammer", "Thunderfury",
        "Eclipse Blade", "Doomhammer", "Stormbreaker", "Soulrender", "Voidblade", "Dreadnought Mace", "Inferno Axe", "Bloodthirsty Sword", "Wyrm's Claw", "Seraphim Spear", "Abyssal Club",
        "Hellfire Mace", "Gloomhaven Hammer", "Ironclad Axe", "Meteorite Sword", "Titan's Mace", "Dragonbone Axe", "Celestial Blade", "Infernal Warhammer", "Eldritch Great Sword", "Vortex Spear",
        "Runeblade", "Dragonscale Mace", "Tempest Axe", "Glacial Warhammer", "Raven's Claw", "Phoenix Sword", "Oathkeeper Mace", "Valkyrie's Spear", "Onyx Warhammer", "Celestial Axe"
    ],
    "Archer": [
        "Legendary Bow", "Shadowhunter Crossbow", "Phoenix Bow", "Stormcaller Bow", "Dragon's Eye Bow", "Moonlit Crossbow", "Eagle Eye Bow", "Frostbite Longbow", "Firestorm Crossbow", "Ancient Hunter's Bow",
        "Celestial Crossbow", "Dragon's Fury Bow", "Lightningstrike Bow", "Artemis's Bow", "Shadowstrike Crossbow", "Stormwind Bow", "Sunflare Crossbow", "Emerald Eye Bow", "Spectral Longbow", "Viper's Bow",
        "Shadowstalker Crossbow", "Thunderstrike Longbow", "Windrider's Bow", "Elven Longbow", "Frostfang Bow", "Inferno Crossbow", "Celestial Longbow", "Serpent's Bow", "Moonshadow Crossbow", "Starfire Bow",
        "Stormblade Crossbow", "Dragon's Talon Bow", "Spectral Crossbow", "Sunset Bow", "Venomstrike Longbow", "Frostfire Crossbow", "Celestial Archer's Bow", "Hunter's Mark Bow", "Shadowflame Longbow", "Starlight Bow"
    ],
    "Mage": [
        "Staff of the Archmage", "Firelord's Wand", "Ice Queen's Staff", "Stormcaster's Rod", "Celestial Orb", "Wand of Eternity", "Mystic Wand of Wisdom", "Inferno Staff", "Frostweaver's Rod", "Thunderstrike Wand",
        "Sorcerer's Crystal Staff", "Elemental Scepter", "Eldritch Wand of Power", "Celestial Mage's Staff", "Runewood Wand", "Arcane Orb", "Wand of the Void", "Staff of Eternity", "Firestorm Wand", "Frostfire Staff",
        "Arcane Staff of Wisdom", "Celestial Fire Staff", "Elemental Rod", "Staff of Shadows", "Wand of the Elements", "Infernal Wand", "Crystal Staff of Power", "Wand of Arcana", "Lightning Rod", "Eldritch Staff of Night",
        "Celestial Wand of Light", "Sorcerer's Flame Staff", "Frozen Rod", "Mystic Scepter", "Arcane Crystal Staff", "Wand of Knowledge", "Stormcaller Staff", "Eldritch Crystal Wand", "Frostweaver's Scepter", "Celestial Arcane Staff"
    ]
}

potions = {"Health Potion": 20, "Mana Potion": 25}
weapon_shop = {"Sword": 100, "Bow": 120, "Staff": 150}
armor_shop = {"Leather Armor": 50, "Iron Armor": 80, "Steel Armor": 100}

player_class = None
player_subclass = None
items = []
coins = 100
#dic_coins={"coins":100}
current_area = "Village"
stats = {"level": 1, "xp": 0, "health": 100, "mana": 50, "damage": 10, "element": random.choice(elements)}
inventory = {"weapons": [], "potions": [], "others": []}
username = ""
password = ""

player_data = {
    "username": username,
    "password": password,
    "class": player_class,
    "stats": stats,
    "inventory": inventory,
    "coins": coins,
    "current_area": current_area
}

def save_game(filename="savegame.json"):
    with open(filename, 'w') as file:
        json.dump(player_data, file)
    print("Game saved successfully.")

def load_game(filename="savegame.json"):
    global player_data
    try:
        with open(filename, 'r') as file:
            player_data = json.load(file)
        print("Game loaded successfully.")
    except FileNotFoundError:
        print("Save file not found. Starting a new game.")
        
def login():
    global username, password
    username = input("Enter your username: ")
    password = input("Enter your password: ")



def level_up():
    global stats
    stats['level'] += 1
    stats['health'] += 20
    stats['mana'] += 10
    stats['damage'] += 5
    print(f"\nCongratulations! You've reached level {stats['level']}!")

def choose_class():
    global player_class
    print("Choose your class:")
    print("1. Warrior")
    print("2. Archer")
    print("3. Mage")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        player_class = "Warrior"
    elif choice == "2":
        player_class = "Archer"
    elif choice == "3":
        player_class = "Mage"
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player_class = "Warrior"
    print(f"You are now a {player_class}!")

def class_ability():
    if player_class == "Warrior":
        print("1. Shield Bash\n2. Power Strike\n3. Battle Cry")
    elif player_class == "Archer":
        print("1. Arrow Rain\n2. Eagle Eye\n3. Snare Trap")
    elif player_class == "Mage":
        print("1. Fireball\n2. Ice Shield\n3. Lightning Bolt")
    choice = input("Choose an ability: ")
    return choice

def encounter_monster(horde=False):
    mob_name = random.choice(list(all_mobs.keys()))
    mob_info = all_mobs[mob_name]
    mob_health = mob_info["health"]
    mob_damage = mob_info["damage"]
    mob_element = mob_info["element"]
    print(f"\nA wild {mob_name} appears!")
    if horde:
        print("It's a horde of monsters!")
    fight_monster(mob_name, mob_health, mob_damage, mob_element)

def calculate_damage(damage, target_element):
    weaknesses = {
        "Fire": ["Water", "Ice"],
        "Ice": ["Fire", "Lightning"],
        "Lightning": ["Earth", "Water"],
        "Earth": ["Air", "Lightning"],
        "Water": ["Fire", "Earth"],
        "Air": ["Earth", "Water"],
        "Darkness": ["Light"],
        "Light": ["Darkness"],
        "Poison": ["Light"],
        "Chaos": []
    }
    if target_element in weaknesses[stats['element']]:
        damage *= 1.5
        print(f"Critical hit! {target_element} is weak against {stats['element']}!")
    return damage

def fight_monster(mob_name, mob_health, mob_damage, mob_element):
    global stats, coins, inventory
    player_health = stats['health']
    xp_gain = 10 * stats['level']
    
    while mob_health > 0 and player_health > 0:
        print(f"\nFighting {mob_name}:")
        action = input("Do you want to Attack, Use a Potion, or Use an Ability? (attack/potion/ability): ").lower()
        
        if action == "attack":
            damage = calculate_damage(stats['damage'] + random.randint(-5, 5), mob_element)
            mob_health -= damage
            print(f"You dealt {damage} damage to the {mob_name}.")
        elif action == "potion":
            use_potions()
            continue
        elif action == "ability":
            ability = class_ability()
            print(f"You used ability {ability}!")
        else:
            print("Invalid action. Please choose 'attack', 'potion', or 'ability'.")
            continue
        
        if mob_health <= 0:
            print(f"You have defeated the {mob_name}!")
            coins += 50
            weapon_drop = random.choice(all_weapons[player_class])
            inventory["weapons"].append(weapon_drop)
            print(f"You found a {weapon_drop}!")
            stats['xp'] += xp_gain
            print(f"You gained {xp_gain} XP.")
            if stats['xp'] >= 100 * stats['level']:
                level_up()
            break

        player_health -= mob_damage
        print(f"The {mob_name} dealt {mob_damage} damage to you.")
        
        if player_health <= 0:
            print("You have been defeated!")
            break
    
    stats['health'] = player_health

def use_potions():
    global coins
    print("\nPotions available:")
    for potion, price in potions.items():
        print(f"{potion}: {price} coins")
    choice = input("Enter the name of the potion you want to use: ")
    if choice in potions:
        if coins >= potions[choice]:
            coins -= potions[choice]
            if choice == "Health Potion":
                stats['health'] += 50
                print(f"You used a {choice}. Your health is now {stats['health']}.")
            elif choice == "Mana Potion":
                stats['mana'] += 50
                print(f"You used a {choice}. Your mana is now {stats['mana']}.")
        else:
            print("Not enough coins.")
    else:
        print("Invalid potion choice.")

def choose_area():
    global current_area
    print("\nWhere do you want to go?")
    
    
    
    for i, island in enumerate(islands, 1):
        if stats['level'] >= island["level_requirement"]:
            print(f"Your new island is {i}. {island['name']} - {island['description']}")
    for j in island:
        print(j)
    area_choice = input("Enter the number of your choice: ")
    
    try:
        area_index = int(area_choice) - 1
        if 0 <= area_index < len(islands) and stats['level'] >= islands[area_index]["level_requirement"]:
            current_area = islands[area_index]["name"]
            print(f"You are now at {current_area}.")
        else:
            print("Invalid choice or level too low. Please choose a valid area.")
            choose_area()
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
        choose_area()
    return current_area

def explore_village():
    print("\nYou have entered the village.")
    while True:
        event = random.choice(["find_shop", "meet_npc", "find_treasure", "visit_temple", "hidden_quest"])
        
        if event == "find_shop":
            print("\nYou found a shop! Let's see what they have for sale.")
            shop()
        elif event == "meet_npc":
            print("\nYou meet an old villager who offers you a quest.")
            job_change_quest()
        elif event == "find_treasure":
            print("\nYou find a hidden treasure chest!")
            coins_found = random.randint(20, 100)
            print(f"You found {coins_found} coins!")
            global coins
            coins += coins_found
        elif event == "visit_temple" and current_area_has_temple():
            visit_temple()
        elif event == "hidden_quest":
            hidden_quest()

        action = input("\nDo you want to continue exploring or return to the village center? (continue/return): ").lower()
        if action == "return":
            print("Returning to the village center.")
            break
        elif action != "continue":
            print("Invalid choice. Please choose 'continue' or 'return'.")

def explore_forest():
    print("\nYou have entered the forest.")
    while True:
        encounter_monster(horde=random.choice([True, False]))
        action = input("Do you want to continue exploring or return to the village? (continue/return): ").lower()
        if action == "return":
            print("Returning to the village.")
            break
        elif action == "continue":
            if random.choice([True, False]):
                print("A horde of monsters appears!")
                encounter_monster(horde=True)
        else:
            print("Invalid choice. Please choose 'continue' or 'return'.")

def explore_islands():
    print("\nYou have entered a island.")
    while True:
        encounter_monster(horde=random.choice([True, False]))
        action = input("Do you want to continue exploring or return to the village? (continue/return): ").lower()
        if action == "return":
            print("Returning to the village.")
            break
        elif action == "continue":
            if random.choice([True, False]):
                print("A horde of monsters appears!")
                encounter_monster(horde=True)
        else:
            print("Invalid choice. Please choose 'continue' or 'return'.")

def explore_dungeon():
    print("\nYou have entered a dungeon.")
    while True:
        encounter_monster(horde=random.choice([True, False]))
        action = input("Do you want to continue exploring or return to the village? (continue/return): ").lower()
        if action == "return":
            print("Returning to the village.")
            break
        elif action == "continue":
            if random.choice([True, False]):
                print("A horde of monsters appears!")
                encounter_monster(horde=True)
        else:
            print("Invalid choice. Please choose 'continue' or 'return'.")

def shop():
    global coins
    print("\nWelcome to the shop!")
    print("1. Buy Potions")
    print("2. Buy Weapons")
    print("3. Buy Armor")
    print("4. Sell Items")
    print("5. Exit Shop")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        print("\nPotions for sale:")
        for potion, price in potions.items():
            print(f"{potion}: {price} coins")
        potion_choice = input("Enter the name of the potion you want to buy: ")
        if potion_choice in potions:
            if coins >= potions[potion_choice]:
                coins -= potions[potion_choice]
                inventory["potions"].append(potion_choice)
                print(f"You bought a {potion_choice}.")
            else:
                print("Not enough coins.")
        else:
            print("Invalid potion choice.")
    elif choice == "2":
        print("\nWeapons for sale:")
        for weapon, price in weapon_shop.items():
            print(f"{weapon}: {price} coins")
        weapon_choice = input("Enter the name of the weapon you want to buy: ")
        if weapon_choice in weapon_shop:
            if coins >= weapon_shop[weapon_choice]:
                coins -= weapon_shop[weapon_choice]
                inventory["weapons"].append(weapon_choice)
                print(f"You bought a {weapon_choice}.")
            else:
                print("Not enough coins.")
        else:
            print("Invalid weapon choice.")
    elif choice == "3":
        print("\nArmor for sale:")
        for armor, price in armor_shop.items():
            print(f"{armor}: {price} coins")
        armor_choice = input("Enter the name of the armor you want to buy: ")
        if armor_choice in armor_shop:
            if coins >= armor_shop[armor_choice]:
                coins -= armor_shop[armor_choice]
                inventory["others"].append(armor_choice)
                print(f"You bought {armor_choice}.")
            else:
                print("Not enough coins.")
    elif choice == "4":
        sell_items()
    elif choice == "5":
        print("Exiting shop.")
    else:
        print("Invalid choice. Please try again.")

def sell_items():
    global coins
    print("\nYour Inventory:")
    print("1. Weapons")
    print("2. Potions")
    print("3. Others")
    item_type = input("Enter the number of the category you want to sell items from: ")
    
    if item_type == "1":
        print("\nYour Weapons:")
        for i, weapon in enumerate(inventory["weapons"], 1):
            print(f"{i}. {weapon}")
        item_choice = int(input("Enter the number of the weapon you want to sell: ")) - 1
        if 0 <= item_choice < len(inventory["weapons"]):
            item_name = inventory["weapons"].pop(item_choice)
            item_value = random.randint(10, 50)  # Value of weapon
            coins += item_value
            print(f"You sold {item_name} for {item_value} coins.")
        else:
            print("Invalid choice.")
    elif item_type == "2":
        print("\nYour Potions:")
        for i, potion in enumerate(inventory["potions"], 1):
            print(f"{i}. {potion}")
        item_choice = int(input("Enter the number of the potion you want to sell: ")) - 1
        if 0 <= item_choice < len(inventory["potions"]):
            item_name = inventory["potions"].pop(item_choice)
            item_value = potions[item_name] // 2  # Sell for half the purchase price
            coins += item_value
            print(f"You sold {item_name} for {item_value} coins.")
        else:
            print("Invalid choice.")
    elif item_type == "3":
        print("\nYour Other Items:")
        for i, other_item in enumerate(inventory["others"], 1):
            print(f"{i}. {other_item}")
        item_choice = int(input("Enter the number of the item you want to sell: ")) - 1
        if 0 <= item_choice < len(inventory["others"]):
            item_name = inventory["others"].pop(item_choice)
            item_value = random.randint(10, 50) 
            coins += item_value
            print(f"You sold {item_name} for {item_value} coins.")
        else:
            print("Invalid choice.")
    else:
        print("Invalid category choice.")

def current_area_has_temple():
    for island in islands:
        if island['name'] == current_area and island['has_temple']:
            return True
    return False

def visit_temple():
    print("\nYou have entered a temple.")
    gods = ["God of Light", "God of Darkness", "God of Fire", "God of Water", "God of Earth", "God of Air"]
    god = random.choice(gods)
    print(f"\nYou stand before the altar of the {god}.")
    print("The priest asks you a question:")
    questions_and_answers = {
        "What is the symbol of peace?": ["dove", "tree", "rainbow"],
        "How do you purify water?": ["boil", "freeze", "filter"],
        "What element opposes fire?": ["water", "earth", "air"],
        "What is the essence of courage?": ["bravery", "strength", "wisdom"],
        "How do you calm a storm?": ["patience", "power", "magic"]
    }
    question = random.choice(list(questions_and_answers.keys()))
    correct_answer = questions_and_answers[question][0]
    random.shuffle(questions_and_answers[question])
    for i, answer in enumerate(questions_and_answers[question], 1):
        print(f"{i}. {answer}")
    answer_choice = input(f"{question}: ").strip().lower()
    if answer_choice == correct_answer:
        print(f"The {god} blesses you with increased strength!")
        stats['damage'] += 5
    else:
        print(f"The {god} rejects you! You feel weakened.")
        stats['damage'] -= 5

def job_change_quest():
    global player_subclass
    print("\nYou have encountered a mysterious NPC offering a quest!")
    print("They tell you of an ancient power hidden in the depths of the world, a power that can enhance your abilities.")
    accept_quest = input("Do you accept the quest to unlock a new subclass? (yes/no): ").lower()

    if accept_quest == "yes":
        print(f"\nThe NPC gives you a task: 'To unlock the hidden power, you must collect the three Shards of Light.")
        print("These shards are located in a nearby dungeon, guarded by formidable creatures. Only those who prove their worth will gain the power of a new subclass.'")
        
        print("\nYour journey begins...")

        shards_collected = 0
        for i in range(3):
            print(f"\nEncounter {i + 1}:")
            result = input("Do you want to fight the guardian of this shard? (yes/no): ").lower()
            if result == "yes":
                print(f"You engage in a fierce battle with {encounter_monster()}")
                shards_collected += 1
                print(f"You have collected {shards_collected} Shard(s) of {random.choice(elements)}.")
            else:
                print("You decide not to engage with the guardian.")
                break

        if shards_collected == 3:
            new_subclass = random.choice(subclasses.get(player_class, []))
            print(f"\nCongratulations! After collecting all the Shards of {random.choice(elements)}, the NPC reveals your new subclass: {new_subclass}.")
            player_subclass = new_subclass
        else:
            print(f"\nYou were unable to collect all the Shards of {random.choice(elements)}. The quest remains incomplete.")

    else:
        print("\nYou decline the quest. Perhaps another time...")

def hidden_quest():
    print("\nYou have discovered a hidden quest!")
    quests = [
        "Retrieve the lost artifact from the abandoned temple.",
        "Defeat the rogue wizard terrorizing the nearby village.",
        "Rescue the captured merchant from the bandit camp.",
        "Find the rare herb needed to cure the plague."
    ]
    selected_quest = random.choice(quests)
    print(f"Quest: {selected_quest}")
    print("Completing this quest may lead to rare rewards!")

def main_paths():
    print("\nChoose your path:")
    print("1. Hero's Journey")
    print("2. Quest for Knowledge")
    print("3. Search for Power")
    print("4. Defender of the Weak")
    print("5. Seeker of Justice")
    print("6. Master of Elements")
    print("7. Hunter of Darkness")
    print("8. Guardian of Light")
    print("9. Warlord's Ambition")
    print("10. Peacemaker's Way")
    choice = input("Enter the number of your choice: ")
    print(f"\nYou have chosen the path of {choice}. Your adventure unfolds...")

def main_game_loop():
    choose_class()
    main_paths()
    while True:
        print("\nWhat would you like to do?")
        print("1. Explore Area")
        print("2. Visit Shop")
        print("3. View Stats")
        print("4. Quit")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            current_area = choose_area()
            if current_area == "Dungeon":
                explore_dungeon()
            elif current_area == "Forest":
                explore_forest()
            elif current_area == "Village":
                explore_village()
            else:
                explore_islands()
        elif choice == "2":
            shop()
        elif choice == "3":
            print(f"\nPlayer Stats:")
            print(f"Username: {username}")
            print(f"Class: {player_class}")
            print(f"Subclass: {player_subclass}")
            print(f"Level: {stats['level']}")
            print(f"Health: {stats['health']}")
            print(f"Mana: {stats['mana']}")
            print(f"Damage: {stats['damage']}")
            print(f"Element: {stats['element']}")
            print(f"Coins: {coins}")
            print(f"Inventory: {inventory}")
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_game_loop()
