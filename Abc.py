import random
import json
import sys

all_weapons = {
    "Warrior": [
        {"name": "Short Sword", "damage_bonus": 5},
        {"name": "Long Sword", "damage_bonus": 7},
        {"name": "Great Sword", "damage_bonus": 10},
        {"name": "Hand Axe", "damage_bonus": 6},
        {"name": "Battle Axe", "damage_bonus": 9},
        {"name": "War Axe", "damage_bonus": 11},
        {"name": "Wooden Mace", "damage_bonus": 4},
        {"name": "Iron Mace", "damage_bonus": 6},
        {"name": "Spiked Mace", "damage_bonus": 8},
        {"name": "Spear", "damage_bonus": 7},
        {"name": "Broadsword", "damage_bonus": 8},
        {"name": "Claymore", "damage_bonus": 10},
        {"name": "Warhammer", "damage_bonus": 12},
        {"name": "Halberd", "damage_bonus": 10},
        {"name": "Battle Hammer", "damage_bonus": 11},
        {"name": "Maul", "damage_bonus": 13},
        {"name": "Glaive", "damage_bonus": 9},
        {"name": "Pike", "damage_bonus": 8},
        {"name": "Polearm", "damage_bonus": 10},
        {"name": "Morning Star", "damage_bonus": 9},
        {"name": "Scimitar", "damage_bonus": 6},
        {"name": "Kris", "damage_bonus": 7},
        {"name": "Crescent Blade", "damage_bonus": 8},
        {"name": "Cutlass", "damage_bonus": 6},
        {"name": "Bastard Sword", "damage_bonus": 9},
        {"name": "Flail", "damage_bonus": 7},
        {"name": "Throwing Axe", "damage_bonus": 5},
        {"name": "Light Mace", "damage_bonus": 5},
        {"name": "Heavy Mace", "damage_bonus": 8},
        {"name": "War Club", "damage_bonus": 6},
        {"name": "Greataxe", "damage_bonus": 12},
        {"name": "Dire Sword", "damage_bonus": 10},
        {"name": "Dragon Mace", "damage_bonus": 12},
        {"name": "Viking Axe", "damage_bonus": 9},
        {"name": "Champion's Sword", "damage_bonus": 11},
        {"name": "Giant's Club", "damage_bonus": 14},
        {"name": "Stormhammer", "damage_bonus": 13},
        {"name": "Colossal Axe", "damage_bonus": 15}
    ],
    "Archer": [
        {"name": "Short Bow", "damage_bonus": 5},
        {"name": "Long Bow", "damage_bonus": 7},
        {"name": "Crossbow", "damage_bonus": 8},
        {"name": "Recurve Bow", "damage_bonus": 6},
        {"name": "Compound Bow", "damage_bonus": 9},
        {"name": "Blowgun", "damage_bonus": 3},
        {"name": "Light Crossbow", "damage_bonus": 7},
        {"name": "Heavy Crossbow", "damage_bonus": 10},
        {"name": "Composite Bow", "damage_bonus": 8},
        {"name": "War Bow", "damage_bonus": 9},
        {"name": "Hunting Bow", "damage_bonus": 6},
        {"name": "Elven Bow", "damage_bonus": 8},
        {"name": "Magic Bow", "damage_bonus": 9},
        {"name": "Flaming Bow", "damage_bonus": 10},
        {"name": "Ice Bow", "damage_bonus": 10},
        {"name": "Lightning Bow", "damage_bonus": 11},
        {"name": "Storm Bow", "damage_bonus": 12},
        {"name": "Shadow Bow", "damage_bonus": 9},
        {"name": "Silent Bow", "damage_bonus": 7},
        {"name": "Swift Bow", "damage_bonus": 6},
        {"name": "Ancient Bow", "damage_bonus": 8},
        {"name": "Ranger's Bow", "damage_bonus": 9},
        {"name": "Sniper's Bow", "damage_bonus": 12},
        {"name": "Falcon Bow", "damage_bonus": 8},
        {"name": "Eagle's Bow", "damage_bonus": 10},
        {"name": "Celestial Bow", "damage_bonus": 12},
        {"name": "Tranquil Bow", "damage_bonus": 7},
        {"name": "Hunter's Crossbow", "damage_bonus": 9},
        {"name": "Wind Bow", "damage_bonus": 10},
        {"name": "Dragon's Crossbow", "damage_bonus": 12},
        {"name": "Silver Bow", "damage_bonus": 8},
        {"name": "Golden Bow", "damage_bonus": 9},
        {"name": "Emerald Bow", "damage_bonus": 9},
        {"name": "Elven Longbow", "damage_bonus": 10},
        {"name": "Hunter's Recurve Bow", "damage_bonus": 8},
        {"name": "Phantom Bow", "damage_bonus": 11},
        {"name": "Cursed Bow", "damage_bonus": 11}
    ],
    "Mage": [
        {"name": "Wooden Staff", "damage_bonus": 4},
        {"name": "Iron Staff", "damage_bonus": 5},
        {"name": "Mystic Staff", "damage_bonus": 6},
        {"name": "Fire Staff", "damage_bonus": 8},
        {"name": "Ice Staff", "damage_bonus": 8},
        {"name": "Lightning Staff", "damage_bonus": 9},
        {"name": "Arcane Staff", "damage_bonus": 7},
        {"name": "Eldritch Staff", "damage_bonus": 10},
        {"name": "Dark Staff", "damage_bonus": 9},
        {"name": "Healing Staff", "damage_bonus": 6},
        {"name": "Sorcerer's Staff", "damage_bonus": 7},
        {"name": "Elemental Staff", "damage_bonus": 9},
        {"name": "Wizard's Staff", "damage_bonus": 7},
        {"name": "Enchanter's Rod", "damage_bonus": 6},
        {"name": "Mystic Wand", "damage_bonus": 5},
        {"name": "Crystal Rod", "damage_bonus": 6},
        {"name": "Staff of Power", "damage_bonus": 10},
        {"name": "Rune Staff", "damage_bonus": 8},
        {"name": "Celestial Wand", "damage_bonus": 7},
        {"name": "Arcane Rod", "damage_bonus": 7},
        {"name": "Staff of Wisdom", "damage_bonus": 8},
        {"name": "Staff of Flames", "damage_bonus": 9},
        {"name": "Frost Rod", "damage_bonus": 8},
        {"name": "Staff of Light", "damage_bonus": 9},
        {"name": "Shadow Wand", "damage_bonus": 7},
        {"name": "Necromancer's Staff", "damage_bonus": 10},
        {"name": "Staff of the Elements", "damage_bonus": 9},
        {"name": "Eldritch Wand", "damage_bonus": 8},
        {"name": "Celestial Staff", "damage_bonus": 9},
        {"name": "Wand of Healing", "damage_bonus": 5},
        {"name": "Fire Wand", "damage_bonus": 8},
        {"name": "Ice Wand", "damage_bonus": 8},
        {"name": "Lightning Wand", "damage_bonus": 9},
        {"name": "Staff of the Ancients", "damage_bonus": 10},
        {"name": "Staff of the Mages", "damage_bonus": 9},
        {"name": "Ethereal Staff", "damage_bonus": 10},
        {"name": "Staff of Knowledge", "damage_bonus": 7},
        {"name": "Wizard's Wand", "damage_bonus": 6},
        {"name": "Enchanter's Wand", "damage_bonus": 6},
        {"name": "Staff of Shadows", "damage_bonus": 9}
    ]
}

base_weapons = {
    "Warrior": [
        {"name": "Dragon Slayer Sword", "damage_bonus": 15, "price": 300},
        {"name": "Excalibur", "damage_bonus": 18, "price": 360},
        {"name": "Mjolnir", "damage_bonus": 20, "price": 400},
        {"name": "Giant's Axe", "damage_bonus": 22, "price": 440},
        {"name": "Meteor Hammer", "damage_bonus": 25, "price": 500},
        {"name": "Celestial Mace", "damage_bonus": 17, "price": 340},
        {"name": "Frostbrand Sword", "damage_bonus": 16, "price": 320},
        {"name": "Flaming Great Sword", "damage_bonus": 19, "price": 380},
        {"name": "Shadow Warhammer", "damage_bonus": 21, "price": 420},
        {"name": "Thunderfury", "damage_bonus": 23, "price": 460},
        {"name": "Eclipse Blade", "damage_bonus": 24, "price": 480},
        {"name": "Doomhammer", "damage_bonus": 22, "price": 440},
        {"name": "Stormbreaker", "damage_bonus": 23, "price": 460},
        {"name": "Soulrender", "damage_bonus": 24, "price": 480},
        {"name": "Voidblade", "damage_bonus": 25, "price": 500},
        {"name": "Dreadnought Mace", "damage_bonus": 20, "price": 400},
        {"name": "Inferno Axe", "damage_bonus": 21, "price": 420},
        {"name": "Bloodthirsty Sword", "damage_bonus": 22, "price": 440},
        {"name": "Wyrm's Claw", "damage_bonus": 23, "price": 460},
        {"name": "Seraphim Spear", "damage_bonus": 24, "price": 480},
        {"name": "Abyssal Club", "damage_bonus": 25, "price": 500},
        {"name": "Hellfire Mace", "damage_bonus": 22, "price": 440},
        {"name": "Gloomhaven Hammer", "damage_bonus": 23, "price": 460},
        {"name": "Ironclad Axe", "damage_bonus": 21, "price": 420},
        {"name": "Meteorite Sword", "damage_bonus": 24, "price": 480},
        {"name": "Titan's Mace", "damage_bonus": 25, "price": 500},
        {"name": "Dragonbone Axe", "damage_bonus": 23, "price": 460},
        {"name": "Celestial Blade", "damage_bonus": 24, "price": 480},
        {"name": "Infernal Warhammer", "damage_bonus": 25, "price": 500},
        {"name": "Eldritch Great Sword", "damage_bonus": 23, "price": 460},
        {"name": "Vortex Spear", "damage_bonus": 22, "price": 440},
        {"name": "Runeblade", "damage_bonus": 24, "price": 480},
        {"name": "Dragonscale Mace", "damage_bonus": 25, "price": 500},
        {"name": "Tempest Axe", "damage_bonus": 23, "price": 460},
        {"name": "Glacial Warhammer", "damage_bonus": 24, "price": 480},
        {"name": "Raven's Claw", "damage_bonus": 23, "price": 460},
        {"name": "Phoenix Sword", "damage_bonus": 24, "price": 480},
        {"name": "Oathkeeper Mace", "damage_bonus": 25, "price": 500},
        {"name": "Valkyrie's Spear", "damage_bonus": 23, "price": 460},
        {"name": "Onyx Warhammer", "damage_bonus": 25, "price": 500},
        {"name": "Celestial Axe", "damage_bonus": 24, "price": 480}
    ],
    "Archer": [
        {"name": "Legendary Bow", "damage_bonus": 15, "price": 300},
        {"name": "Shadowhunter Crossbow", "damage_bonus": 16, "price": 320},
        {"name": "Phoenix Bow", "damage_bonus": 17, "price": 340},
        {"name": "Stormcaller Bow", "damage_bonus": 18, "price": 360},
        {"name": "Dragon's Eye Bow", "damage_bonus": 19, "price": 380},
        {"name": "Moonlit Crossbow", "damage_bonus": 16, "price": 320},
        {"name": "Eagle Eye Bow", "damage_bonus": 17, "price": 340},
        {"name": "Frostbite Longbow", "damage_bonus": 18, "price": 360},
        {"name": "Firestorm Crossbow", "damage_bonus": 19, "price": 380},
        {"name": "Ancient Hunter's Bow", "damage_bonus": 17, "price": 340},
        {"name": "Celestial Crossbow", "damage_bonus": 18, "price": 360},
        {"name": "Dragon's Fury Bow", "damage_bonus": 19, "price": 380},
        {"name": "Lightningstrike Bow", "damage_bonus": 20, "price": 400},
        {"name": "Artemis's Bow", "damage_bonus": 21, "price": 420},
        {"name": "Shadowstrike Crossbow", "damage_bonus": 19, "price": 380},
        {"name": "Stormwind Bow", "damage_bonus": 18, "price": 360},
        {"name": "Sunflare Crossbow", "damage_bonus": 20, "price": 400},
        {"name": "Emerald Eye Bow", "damage_bonus": 19, "price": 380},
        {"name": "Spectral Longbow", "damage_bonus": 20, "price": 400},
        {"name": "Viper's Bow", "damage_bonus": 19, "price": 380},
        {"name": "Shadowstalker Crossbow", "damage_bonus": 18, "price": 360},
        {"name": "Thunderstrike Longbow", "damage_bonus": 19, "price": 380},
        {"name": "Windrider's Bow", "damage_bonus": 20, "price": 400},
        {"name": "Elven Longbow", "damage_bonus": 18, "price": 360},
        {"name": "Frostfang Bow", "damage_bonus": 19, "price": 380},
        {"name": "Inferno Crossbow", "damage_bonus": 20, "price": 400},
        {"name": "Celestial Longbow", "damage_bonus": 21, "price": 420},
        {"name": "Serpent's Bow", "damage_bonus": 19, "price": 380},
        {"name": "Moonshadow Crossbow", "damage_bonus": 20, "price": 400},
        {"name": "Starfire Bow", "damage_bonus": 21, "price": 420},
        {"name": "Stormblade Crossbow", "damage_bonus": 20, "price": 400},
        {"name": "Dragon's Talon Bow", "damage_bonus": 21, "price": 420},
        {"name": "Spectral Crossbow", "damage_bonus": 19, "price": 380},
        {"name": "Sunset Bow", "damage_bonus": 18, "price": 360},
        {"name": "Venomstrike Longbow", "damage_bonus": 19, "price": 380},
        {"name": "Frostfire Crossbow", "damage_bonus": 20, "price": 400},
        {"name": "Celestial Archer's Bow", "damage_bonus": 21, "price": 420},
        {"name": "Hunter's Mark Bow", "damage_bonus": 19, "price": 380},
        {"name": "Shadowflame Longbow", "damage_bonus": 20, "price": 400},
        {"name": "Starlight Bow", "damage_bonus": 21, "price": 420}
    ],
    "Mage": [
        {"name": "Staff of the Archmage", "damage_bonus": 15, "price": 300},
        {"name": "Firelord's Wand", "damage_bonus": 16, "price": 320},
        {"name": "Ice Queen's Staff", "damage_bonus": 17, "price": 340},
        {"name": "Stormcaster's Rod", "damage_bonus": 18, "price": 360},
        {"name": "Celestial Orb", "damage_bonus": 19, "price": 380},
        {"name": "Wand of Eternity", "damage_bonus": 18, "price": 360},
        {"name": "Mystic Wand of Wisdom", "damage_bonus": 17, "price": 340},
        {"name": "Inferno Staff", "damage_bonus": 19, "price": 380},
        {"name": "Frostweaver's Rod", "damage_bonus": 18, "price": 360},
        {"name": "Thunderstrike Wand", "damage_bonus": 20, "price": 400},
        {"name": "Sorcerer's Crystal Staff", "damage_bonus": 19, "price": 380},
        {"name": "Elemental Scepter", "damage_bonus": 20, "price": 400},
        {"name": "Eldritch Wand of Power", "damage_bonus": 21, "price": 420},
        {"name": "Celestial Mage's Staff", "damage_bonus": 20, "price": 400},
        {"name": "Runewood Wand", "damage_bonus": 18, "price": 360},
        {"name": "Arcane Orb", "damage_bonus": 19, "price": 380},
        {"name": "Wand of the Void", "damage_bonus": 20, "price": 400},
        {"name": "Staff of Eternity", "damage_bonus": 21, "price": 420},
        {"name": "Firestorm Wand", "damage_bonus": 20, "price": 400},
        {"name": "Frostfire Staff", "damage_bonus": 21, "price": 420},
        {"name": "Arcane Staff of Wisdom", "damage_bonus": 19, "price": 380},
        {"name": "Celestial Fire Staff", "damage_bonus": 20, "price": 400},
        {"name": "Elemental Rod", "damage_bonus": 21, "price": 420},
        {"name": "Staff of Shadows", "damage_bonus": 19, "price": 380},
        {"name": "Wand of the Elements", "damage_bonus": 20, "price": 400},
        {"name": "Infernal Wand", "damage_bonus": 21, "price": 420},
        {"name": "Crystal Staff of Power", "damage_bonus": 20, "price": 400},
        {"name": "Wand of Arcana", "damage_bonus": 19, "price": 380},
        {"name": "Lightning Rod", "damage_bonus": 21, "price": 420},
        {"name": "Eldritch Staff of Night", "damage_bonus": 20, "price": 400},
        {"name": "Celestial Wand of Light", "damage_bonus": 21, "price": 420},
        {"name": "Sorcerer's Flame Staff", "damage_bonus": 20, "price": 400},
        {"name": "Frozen Rod", "damage_bonus": 19, "price": 380},
        {"name": "Mystic Scepter", "damage_bonus": 18, "price": 360},
        {"name": "Arcane Crystal Staff", "damage_bonus": 20, "price": 400},
        {"name": "Wand of Knowledge", "damage_bonus": 18, "price": 360},
        {"name": "Stormcaller Staff", "damage_bonus": 21, "price": 420},
        {"name": "Eldritch Crystal Wand", "damage_bonus": 20, "price": 400},
        {"name": "Frostweaver's Scepter", "damage_bonus": 21, "price": 420},
        {"name": "Celestial Arcane Staff", "damage_bonus": 22, "price": 440}
    ]
}



class Skill:
    def __init__(self, name, description, power, mana_cost):
        self.name = name
        self.description = description
        self.power = power
        self.mana_cost = mana_cost

    def use_skill(self, user, target):
        user.stats['mana'] -= self.mana_cost
        target.health -= self.power
        print(f"{self.name} used! {self.description}")
        print(f"The {target.name} takes {self.power} damage.")

class PlayerSkill(Skill):
    def __init__(self, name, description, power, mana_cost):
        super().__init__(name, description, power, mana_cost)
        self.mana_cost = mana_cost

    def use_skill(self, player, target):
        if player.stats['mana'] >= self.mana_cost:
            player.stats['mana'] -= self.mana_cost
            print(f"{self.name} used! {self.description}")
            target.health -= self.power
            print(f"The {target.name} takes {self.power} damage.")
            
        else:
            print("Not enough mana to use this skill!")
            
skill_pool = {
    "Warrior": [
        PlayerSkill("Power Strike", "A powerful strike that deals extra damage", 30, 15),
        PlayerSkill("Shield Bash", "Stuns the enemy with a shield bash", 10, 10),
        PlayerSkill("Berserk", "Increases damage but reduces defense for a short time", 40, 20),
        PlayerSkill("Whirlwind", "Attacks all nearby enemies with a spinning strike", 25, 20),
        PlayerSkill("Earth Shatter", "Smashes the ground, causing an earthquake that damages all enemies", 35, 25),
        PlayerSkill("Rage", "Temporarily increases attack speed", 20, 15),
        PlayerSkill("Cleave", "A wide swing that hits multiple enemies", 25, 20),
        PlayerSkill("Iron Defense", "Increases defense temporarily", 0, 10)
    ],
    "Archer": [
        PlayerSkill("Double Shot", "Shoots two arrows at once", 20, 10),
        PlayerSkill("Explosive Arrow", "Fires an arrow that explodes on impact", 35, 15),
        PlayerSkill("Poison Arrow", "Shoots an arrow that poisons the enemy", 25, 10),
        PlayerSkill("Snipe", "A precise shot that deals massive damage", 40, 20),
        PlayerSkill("Rain of Arrows", "Fires multiple arrows into the air to hit several enemies", 30, 25),
        PlayerSkill("Camouflage", "Temporarily hide from enemies", 0, 10),
        PlayerSkill("Quick Shot", "A fast shot with increased speed", 15, 8),
        PlayerSkill("Eagle Eye", "Increases accuracy for a short time", 0, 10)
    ],
    "Mage": [
        PlayerSkill("Fireball", "Launches a ball of fire at the enemy", 25, 15),
        PlayerSkill("Ice Shard", "Fires a sharp shard of ice that slows the enemy", 20, 10),
        PlayerSkill("Lightning Bolt", "Strikes the enemy with a bolt of lightning", 30, 20),
        PlayerSkill("Arcane Blast", "Blasts the enemy with arcane energy", 35, 25),
        PlayerSkill("Healing Wave", "Restores health to you or an ally", 0, 20),
        PlayerSkill("Mana Shield", "Absorbs damage using mana", 0, 15),
        PlayerSkill("Teleport", "Move instantly to another location", 0, 20),
        PlayerSkill("Meteor Shower", "Calls down meteors to strike all enemies", 40, 30)
    ]
}

monster_skill_pool = [
    Skill("Dark Slash", "A shadowy strike that deals extra darkness damage", 25, 10),
    Skill("Venom Spit", "Spits venom at the player, causing poison damage over time", 20, 8),
    Skill("Stun Roar", "Lets out a roar that stuns the player", 0, 5),
    Skill("Flame Breath", "Breathes fire to deal massive fire damage", 30, 12),
    Skill("Ice Spike", "Launches a spike of ice to slow the player", 20, 8),
    Skill("Thunder Clap", "Summons a thunderstorm to strike the player", 35, 15),
    Skill("Shadow Bind", "Binds the player in shadows, reducing movement speed", 0, 7),
    Skill("Earthquake", "Causes the ground to shake, damaging and disorienting the player", 30, 12),
    Skill("Drain Life", "Saps the life from the player, healing the monster", 25, 10),
    Skill("Fury Swipe", "A series of fast swipes that deal rapid damage", 15, 6),
    Skill("Dark Aura", "Envelops the monster in darkness, reducing damage taken", 0, 10),
    Skill("Poison Cloud", "Creates a cloud of poison that damages the player over time", 20, 8),
    Skill("Inferno", "Summons a ring of fire around the player", 35, 15),
    Skill("Frozen Touch", "Freezes the player in place, dealing cold damage", 20, 8),
    Skill("Lightning Surge", "Unleashes a surge of lightning at the player", 30, 12)
]

class Item:
    def __init__(self, name, item_type, damage_bonus=0, health_bonus=0, mana_bonus=0, durability=100):
        self.name = name
        self.item_type = item_type
        self.damage_bonus = damage_bonus
        self.health_bonus = health_bonus
        self.mana_bonus = mana_bonus
        self.durability = durability

    def use_item(self):
        self.durability -= 10
        if self.durability <= 0:
            print(f"{self.name} has broken!")
            return False
        return True

class Player:
    def __init__(self, username, player_class, stats, inventory, coins, current_area):
        self.equipped_items = {}
        self.username = username
        self.player_class = player_class
        self.stats = stats
        self.inventory = inventory
        self.coins = coins
        self.current_area = current_area
        self.skills = self.get_initial_skills()

    def get_initial_skills(self):
        return random.sample(skill_pool[self.player_class], 1)#, 1
    
    def equip_item(self, item):
        if item.item_type in self.equipped_items:
            if self.equipped_items[item.item_type]:
                self.unequip_item(item.item_type)
            self.equipped_items[item.item_type] = item
            self.apply_item_bonuses(item)
            print(f"You equipped {item.name}.")
        else:
            print("You can't equip this item.")

    def unequip_item(self, item_type):
        if self.equipped_items[item_type]:
            item = self.equipped_items[item_type]
            self.remove_item_bonuses(item)
            print(f"You unequipped {item.name}.")
            self.equipped_items[item_type] = None

    def apply_item_bonuses(self, item):
        self.stats['damage'] += item.damage_bonus
        self.stats['health'] += item.health_bonus
        self.stats['mana'] += item.mana_bonus

    def remove_item_bonuses(self, item):
        self.stats['damage'] -= item.damage_bonus
        self.stats['health'] -= item.health_bonus
        self.stats['mana'] -= item.mana_bonus

    def use_item(self, item_name):
        for item in self.inventory['weapons'] + self.inventory['others']:
            if item.name.lower() == item_name.lower() and item.use_item():
                return True
        return False

    def level_up(self):
        self.stats['level'] += 1
        self.stats['health'] += 20
        self.stats['mana'] += 10
        self.stats['damage'] += 5
        print(f"\nCongratulations! You've reached level {self.stats['level']}!")

    def view_stats(self):
        print(f"\nPlayer Stats:")
        print(f"Username: {self.username}")
        print(f"Class: {self.player_class}")
        print(f"Level: {self.stats['level']}")
        print(f"Health: {self.stats['health']}")
        print(f"Mana: {self.stats['mana']}")
        print(f"Damage: {self.stats['damage']}")
        print(f"Coins: {self.coins}")
        print(f"Current Area: {self.current_area}")
        print("Inventory:")
        
        print("Weapons:")
        for weapon in self.inventory['weapons']:
            print(f"  - {weapon.name} (Damage Bonus: {weapon.damage_bonus}, Durability: {weapon.durability})")
        
        print("Potions:")
        for potion in self.inventory['potions']:
            print(f"  - {potion.name} (Durability: {potion.durability})")
        
        print("Others:")
        for other in self.inventory['others']:
            print(f"  - {other.name} (Durability: {other.durability})")
        
        for item_type, item in self.equipped_items.items():
            if item:
                print(f"Equipped {item_type}: {item.name} (Durability: {item.durability})")

class Monster:
    def __init__(self, name, health, damage, element):
        self.name = name
        self.health = health
        self.damage = damage
        self.element = element

    def attack(self, player):
        player.stats['health'] -= self.damage
        print(f"The {self.name} dealt {self.damage} damage to you.")
        if player.stats['health'] <= 0:
            print("You have been defeated!")
            return False
        return True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"You have defeated the {self.name}!")
            return True
        return False
    def get_skills(self):
        skill_count = self.level // 10 
        return random.sample(monster_skill_pool, min(skill_count, len(monster_skill_pool)))

class Area:
    def __init__(self, name, description, level_requirement, has_village, has_temple):
        self.name = name
        self.description = description
        self.level_requirement = level_requirement
        self.has_village = has_village
        self.has_temple = has_temple

class Game:
    def __init__(self, player):
        self.player = player
        self.all_mobs = self.load_mobs()
        self.islands = self.load_islands()
        self.potions = {"Health Potion": 20, "Mana Potion": 25}
        self.weapon_shop = {"Sword": 100, "Bow": 120, "Staff": 150}
        self.armor_shop = {"Leather Armor": 50, "Iron Armor": 80, "Steel Armor": 100}

    def load_mobs(self):
        return {
            "Goblin of Darkness": Monster("Goblin of Darkness", 50, 10, "Darkness"),
            "Shadow Orc": Monster("Shadow Orc", 100, 20, "Darkness"),
            "Eclipse Dragon": Monster("Eclipse Dragon", 200, 30, "Darkness"),
            "Nightmare Zombie": Monster("Nightmare Zombie", 60, 12, "Darkness"),
            "Dark Skeleton": Monster("Dark Skeleton", 75, 15, "Darkness"),
            "Cave Troll": Monster("Cave Troll", 90, 18, "Darkness"),
            "Venomous Spider": Monster("Venomous Spider", 80, 14, "Poison"),
            "Witch of Shadows": Monster("Witch of Shadows", 70, 16, "Darkness"),
            "Vampire Lord": Monster("Vampire Lord", 120, 25, "Darkness"),
            "Shadow Lich": Monster("Shadow Lich", 150, 28, "Darkness"),
            "Dark Golem": Monster("Dark Golem", 180, 20, "Darkness"),
            "Imp of Chaos": Monster("Imp of Chaos", 40, 8, "Chaos"),
            "Banshee Wail": Monster("Banshee Wail", 60, 14, "Darkness"),
            "Griffin of the Night": Monster("Griffin of the Night", 100, 22, "Darkness"),
            "Gorgon of Shadows": Monster("Gorgon of Shadows", 110, 24, "Darkness"),
            "Harpy Screamer": Monster("Harpy Screamer", 70, 15, "Darkness"),
            "Hydra of the Abyss": Monster("Hydra of the Abyss", 200, 30, "Darkness"),
            "Manticore of the Deep": Monster("Manticore of the Deep", 130, 25, "Darkness"),
            "Minotaur of the Labyrinth": Monster("Minotaur of the Labyrinth", 140, 28, "Darkness"),
            "Mummy of the Tomb": Monster("Mummy of the Tomb", 90, 20, "Darkness"),
            "Phoenix of Darkness": Monster("Phoenix of Darkness", 160, 30, "Darkness"),
            "Rat King": Monster("Rat King", 30, 6, "Poison"),
            "Djinn of Shadows": Monster("Djinn of Shadows", 80, 18, "Darkness"),
            "Kraken of the Depths": Monster("Kraken of the Depths", 200, 35, "Darkness"),
            "Wraith of the Night": Monster("Wraith of the Night", 70, 15, "Darkness"),
            "Behemoth of the Earth": Monster("Behemoth of the Earth", 250, 35, "Earth"),
            "Cyclops of the Mountains": Monster("Cyclops of the Mountains", 120, 22, "Earth"),
            "Wyvern of the Skies": Monster("Wyvern of the Skies", 140, 28, "Air"),
            "Naga of the Seas": Monster("Naga of the Seas", 110, 20, "Water"),
            "Lamia of the Abyss": Monster("Lamia of the Abyss", 80, 18, "Darkness"),
            "Dark Knight": Monster("Dark Knight", 200, 30, "Darkness"),
            "Frost Giant": Monster("Frost Giant", 200, 35, "Ice"),
            "Fire Elemental": Monster("Fire Elemental", 150, 25, "Fire"),
            "Earth Elemental": Monster("Earth Elemental", 160, 28, "Earth"),
            "Water Elemental": Monster("Water Elemental", 150, 22, "Water"),
            "Air Elemental": Monster("Air Elemental", 140, 20, "Air"),
            "Shade": Monster("Shade", 80, 16, "Darkness"),
            "Ghoul": Monster("Ghoul", 90, 18, "Darkness"),
            "Hellhound": Monster("Hellhound", 120, 24, "Fire"),
            "Basilisk": Monster("Basilisk", 100, 20, "Earth"),
            "Reaper": Monster("Reaper", 130, 28, "Darkness"),
            "Dire Wolf": Monster("Dire Wolf", 70, 14, "Earth"),
            "Shadow Fiend": Monster("Shadow Fiend", 90, 20, "Darkness"),
            "Roc": Monster("Roc", 150, 30, "Air"),
            "Storm Dragon": Monster("Storm Dragon", 220, 35, "Lightning"),
            "Death Knight": Monster("Death Knight", 180, 30, "Darkness"),
            "Elder Dragon": Monster("Elder Dragon", 250, 40, "Darkness"),
            "Ancient Golem": Monster("Ancient Golem", 250, 35, "Earth"),
            "Specter": Monster("Specter", 70, 15, "Darkness"),
            "Dreadlord": Monster("Dreadlord", 160, 30, "Darkness"),
            "Chaos Beast": Monster("Chaos Beast", 180, 35, "Chaos"),
            "Nightmare": Monster("Nightmare", 90, 20, "Darkness"),
            "Celestial Being": Monster("Celestial Being", 250, 40, "Light")
        }

    def load_islands(self):
        islands = [
            Area("Forest", "A land filled with magical creatures and mysterious temples.", 1, True, True),
            Area("Mystic Island", "A land filled with magical creatures and mysterious temples.", 1, True, True),
            Area("Frost Island",  "An icy landscape inhabited by frost giants, with an ancient temple.",  5,  True,  True),
            Area("Shadow Island",  "A dark and eerie place, rumored to be the lair of Lord Nox.",  15,  False,  False),
            Area("Dungen",  "A hole in a cave with monsters all over it that rose to the top.",  20,  True,  True)
        ]
        for i in range(6, 103):
            islands.append(Area(f"Island {i}", f"A mysterious island filled with adventures and dangers. Explore at your own risk.", i, random.choice([True, False]), random.choice([True, False])))
        return islands

    def choose_area(self):
        print("\nWhere do you want to go?")
        for i, island in enumerate(self.islands, 1):
            if self.player.stats['level'] >= island.level_requirement:
                print(f"{i}. {island.name} - {island.description}")
        area_choice = int(input("Enter the number of your choice: ")) - 1
        if 0 <= area_choice < len(self.islands) and self.player.stats['level'] >= self.islands[area_choice].level_requirement:
            self.player.current_area = self.islands[area_choice].name
            print(f"You are now at {self.player.current_area}.")
        else:
            print("Invalid choice or level too low. Please choose a valid area.")
            self.choose_area()

    def encounter_monster(self):
        mob_name = random.choice(list(self.all_mobs.keys()))
        mob = self.all_mobs[mob_name]  
        print(f"\nA wild {mob_name} appears!")
        self.fight_monster(mob)

    def calculate_damage(self, damage, target_element):
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
        if target_element in weaknesses[self.player.stats['element']]:
            damage *= 1.5
            print(f"Critical hit! {target_element} is weak against {self.player.stats['element']}!")
        return damage

    def fight_monster(self, mob):
        player_health = self.player.stats['health']
        xp_gain = 10 * self.player.stats['level']

        while mob.health > 0 and player_health > 0:
            print(f"\nFighting {mob.name}:")
            action = input("1. Attack\n2. Use a Potion\n3. View Stats\n4. Use Skill\nChoose an action: ").strip().lower()

            if action in ['1', 'attack']:
                damage = self.calculate_damage(self.player.stats['damage'] + random.randint(-5, 5), mob.element)
                print(f"You dealt {damage} damage to the {mob.name}.")
                if mob.take_damage(damage):
                    print(f"The {mob.name} has been defeated!")
                    self.player.coins += 50
                    weapon_choice = random.choice(all_weapons[self.player.player_class])
                    weapon_drop = Item(weapon_choice["name"], "weapon", damage_bonus=weapon_choice["damage_bonus"])
                    self.player.inventory["weapons"].append(weapon_drop)
                    print(f"You found a {weapon_drop.name}!")
                    self.player.stats['xp'] += xp_gain
                    print(f"You gained {xp_gain} XP.")
                    if self.player.stats['xp'] >= 100 * self.player.stats['level']:
                        self.player.level_up()
                    break
            elif action in ['2', 'use a potion', 'potion']:
                self.use_potions()
            elif action in ['3', 'view stats', 'stats']:
                self.player.view_stats()
                continue  
            elif action in ['4', 'use skill', 'skill']:
                self.use_player_skill(mob)
            else:
                print("Invalid action. Please choose a valid option.")
                continue

            if mob.health > 0:
                print(f"Monster Health after attack: {mob.health}")
                player_health -= mob.damage
                print(f"The {mob.name} dealt {mob.damage} damage to you.")
                print(f"Player Health after attack: {player_health}")
            if player_health <= 0:
                print("You have been defeated!")
                break

        self.player.stats['health'] = player_health

        if player_health <= 0:
            print("\nGame Over! You have been defeated.")
            sys.exit()
            # return False  
        return True  



    def use_potions(self):
        print("\nPotions available:")
        for potion in self.player.inventory['potions']:
            print(f"{potion.name} (Durability: {potion.durability})")
        choice = input("Enter the name of the potion you want to use: ").strip().lower()
        if self.player.use_item(choice):
            if choice == "health potion":
                self.player.stats['health'] += 50
                print(f"Your health is now {self.player.stats['health']}.")
            elif choice == "mana potion":
                self.player.stats['mana'] += 50
                print(f"Your mana is now {self.player.stats['mana']}.")
        else:
            print("Invalid or broken potion.")

    def shop(self):
        print("\nWelcome to the shop!")
        print("1. Buy Potions")
        print("2. Buy Weapons")
        print("3. Buy Base Weapons")
        print("4. Buy Armor")
        print("5. Sell Items")
        print("6. Exit Shop")
        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.buy_potions()
        elif choice == 2:
            self.buy_weapons()
        elif choice == 3:
            self.buy_base_weapons()
        elif choice == 4:
            self.buy_armor()
        elif choice == 5:
            self.sell_items()
        elif choice == 6:
            print("Exiting shop.")
        else:
            print("Invalid choice. Please try again.")

    def buy_base_weapons(self):
        print("\nBase Weapons for sale:")
        for weapon in base_weapons[self.player.player_class]:
            print(f"{weapon['name']}: {weapon['price']} coins (Damage Bonus: {weapon['damage_bonus']})")
        
        weapon_choice = input("Enter the name of the base weapon you want to buy: ").strip().lower()
        for weapon in base_weapons[self.player.player_class]:
            if weapon_choice == weapon["name"].lower():
                weapon_price = weapon["price"]
                if self.player.coins >= weapon_price:
                    self.player.coins -= weapon_price
                    weapon_item = Item(weapon["name"], "weapon", damage_bonus=weapon["damage_bonus"])
                    self.player.inventory["weapons"].append(weapon_item)
                    print(f"You bought a {weapon_item.name}.")
                else:
                    print("Not enough coins.")
                return
        print("Invalid weapon choice.")

    def buy_potions(self):
        print("\nPotions for sale:")
        for potion, price in self.potions.items():
            print(f"{potion}: {price} coins")
        potion_choice = input("Enter the name of the potion you want to buy: ").strip().lower()
        if potion_choice.capitalize() in self.potions:
            potion_price = self.potions[potion_choice.capitalize()]
            if self.player.coins >= potion_price:
                self.player.coins -= potion_price
                potion = Item(potion_choice.capitalize(), "potion")
                self.player.inventory["potions"].append(potion)
                print(f"You bought a {potion.name}.")
            else:
                print("Not enough coins.")
        else:
            print("Invalid potion choice.")

    def buy_weapons(self):
        print("\nWeapons for sale:")
        for weapon, price in self.weapon_shop.items():
            print(f"{weapon}: {price} coins")
        weapon_choice = input("Enter the name of the weapon you want to buy: ").strip().lower()
        if weapon_choice.capitalize() in self.weapon_shop:
            weapon_price = self.weapon_shop[weapon_choice.capitalize()]
            if self.player.coins >= weapon_price:
                self.player.coins -= weapon_price
                weapon = Item(weapon_choice.capitalize(), "weapon", damage_bonus=10)
                self.player.inventory["weapons"].append(weapon)
                print(f"You bought a {weapon.name}.")
            else:
                print("Not enough coins.")
        else:
            print("Invalid weapon choice.")

    def buy_armor(self):
        print("\nArmor for sale:")
        for armor, price in self.armor_shop.items():
            print(f"{armor}: {price} coins")
        armor_choice = input("Enter the name of the armor you want to buy: ").strip().lower()
        if armor_choice.capitalize() in self.armor_shop:
            armor_price = self.armor_shop[armor_choice.capitalize()]
            if self.player.coins >= armor_price:
                self.player.coins -= armor_price
                armor = Item(armor_choice.capitalize(), "armor", health_bonus=20)
                self.player.inventory["others"].append(armor)
                print(f"You bought {armor.name}.")
            else:
                print("Not enough coins.")
        else:
            print("Invalid armor choice.")

    def sell_items(self):
        print("\nYour Inventory:")
        print("1. Weapons")
        print("2. Potions")
        print("3. Others")
        item_type = int(input("Enter the number of the category you want to sell items from: "))

        if item_type == 1:
            self.sell_category("weapons")
        elif item_type == 2:
            self.sell_category("potions")
        elif item_type == 3:
            self.sell_category("others")
        else:
            print("Invalid choice. Please try again.")

    def sell_category(self, category):
        print(f"\nYour {category.capitalize()}:")
        items = self.player.inventory[category]
        for i, item in enumerate(items, 1):
            print(f"{i}. {item.name} (Durability: {item.durability})")
        item_choice = int(input(f"Enter the number of the {category[:-1]} you want to sell: ")) - 1
        if 0 <= item_choice < len(items):
            item = items.pop(item_choice)
            item_value = random.randint(10, 50)
            self.player.coins += item_value
            print(f"You sold {item.name} for {item_value} coins.")
        else:
            print("Invalid choice.")

    def explore_area(self):
        print(f"\nYou have entered {self.player.current_area}.")
        while True:
            self.encounter_monster()
            action = int(input("1. Continue exploring\n2. Return to village\nChoose an action: "))
            if action == 2:
                print("Returning to the village.")
                break
    def use_player_skill(self, mob):
        print("Choose a skill to use:")
        for i, skill in enumerate(self.player.skills, 1):
            print(f"{i}. {skill.name} - {skill.description} (Mana Cost: {skill.mana_cost})")
        choice = int(input("Enter the number of the skill you want to use: ")) - 1
        if 0 <= choice < len(self.player.skills):
            selected_skill = self.player.skills[choice]
            if self.player.stats['mana'] >= selected_skill.mana_cost:
                selected_skill.use_skill(self.player, mob)
                print(f"You used {selected_skill.name}!")
            else:
                print("Not enough mana to use this skill!")
        else:
            print("Invalid skill choice.")

def main_game_loop():
    username = input("Enter your username: ")
    while True:
        print("Choose your class:")
        print("1. Warrior")
        print("2. Archer")
        print("3. Mage")
        class_choice = int(input("Enter the number of your choice: "))
        if class_choice == 1:
            player_class = "Warrior"
            break
        elif class_choice == 2:
            player_class = "Archer"
            break
        elif class_choice == 3:
            player_class = "Mage"
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
    
    stats = {"level": 1, "xp": 0, "health": 100, "mana": 50, "damage": 10, "element": random.choice(["Fire", "Ice", "Lightning", "Earth", "Water", "Air", "Darkness", "Light", "Poison", "Chaos"])}
    inventory = {"weapons": [], "potions": [], "others": []}
    player = Player(username, player_class, stats, inventory, coins=230, current_area="Village")

    game = Game(player)

    while True:
        print("\nWhat would you like to do?")
        action = int(input("1. Explore Area\n2. Visit Shop\n3. View Stats\n4. Quit\nChoose an action: "))
        if action == 1:
            game.choose_area()
            game.explore_area()
        elif action == 2:
            game.shop()
        elif action == 3:
            player.view_stats()
        elif action == 4:
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_game_loop()
