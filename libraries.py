race_list = ["Human", "Elf", "Orc", "Gnome"]

background_list = ["Noble", "Beggar", "Wild Child", "Monk"]

class_list = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]

subclass_dictionary = {
    "Barbarian": [3, 12, "Path of the Berserker", "Path of the Totem Warrior"],
    "Bard": [3, 8, "College of Lore", "College of Valor"],
    "Cleric": [1, 8, "Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", 
               "Tempest Domain", "Trickery Domain", "War Domain"],
    "Druid": [2, 8, "Circle of the Land", "Circle of the Moon"],
    "Fighter": [3, 10, "Champion", "Battle Master", "Eldritch Knight"],
    "Monk": [3, 8, "Way of the Open Hand", "Way of the Shadow", "Way of the Four Elements"],
    "Paladin": [3, 10, "Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"],
    "Ranger": [3, 10, "Hunter", "Beast Master"],
    "Rogue": [3, 8, "Thief", "Assassin", "Arcane Trickster"],
    "Sorcerer": [1, 6, "Draconic Bloodline", "Wild Magic"],
    "Warlock": [1, 8,"The Archfey", "The Fiend", "The Great Old One"],
    "Wizard": [2, 6,"School of Abjuration", "School of Conjuration", "School of Divination", 
               "School of Enchantment", "School of Evocation", "School of Illusion", 
               "School of Necromancy", "School of Transmutation"]
    }

stat_options = ["Point buy", "Roll 4d6, pick 3", "Roll 3d6"]

default_stats = {"STR" : 8, "DEX" : 8, "CON" : 8, "INT" : 8, "WIS" : 8, "CHA" : 8}
