from dice_roller import roll_die
import pytest
from character import Character
from libraries import default_stats
from functions import check_input_within_given_range, select_background, select_class, select_race, select_subclass, increase_to_level
from files import delete_character, edit_character, save_character, select_character, view_character


test_subject = Character("Dave", "Human", "Noble", "LG", "23", "Barbarian", "Path of the Totem Warrior", 6, 18, 13, 16, 8, 12, 6, 71)

def test_basic():
    assert "Hello" == "Hello"

# These tests test the Character class functions:

def test_name():
#    checks name is default value "Dave"
   assert test_subject.get_name() == "Dave"
#    sets name to "Simon"
   test_subject.set_name("Simon")
#    checks name was changed to "Simon"
   assert test_subject.get_name() == "Simon"

def test_race():
    # Checks race is default value "Human"
    assert test_subject.get_race() == "Human"
    # Sets race to "Elf"
    test_subject.set_race("Elf")
    # Checks race successfully set to "Elf"
    assert test_subject.get_race() == "Elf"
    
def test_background():
    assert test_subject.get_background() == "Noble"
    test_subject.set_background("Beggar")
    assert test_subject.get_background() == "Beggar"

def test_alignment():
    assert test_subject.get_alignment() == "LG"
    test_subject.set_alignment("CE")
    assert test_subject.get_alignment() == "CE"

def test_age():
    assert test_subject.get_age() == "23"
    test_subject.set_age("2")
    assert test_subject.get_age() == "2"

def test_level():
    assert test_subject.get_level() == 6
    test_subject.set_level(5)
    assert test_subject.get_level() == 5

def test_character_class():
    assert test_subject.get_character_class() == "Barbarian"
    test_subject.set_character_class("Cleric")
    assert test_subject.get_character_class() == "Cleric"

def test_character_subclass():
    assert test_subject.get_character_subclass() == "Path of the Totem Warrior"
    test_subject.set_character_subclass("Test")
    assert test_subject.get_character_subclass() == "Test"

def test_stats():
    assert test_subject.get_stats() == {"STR":18, "DEX":13, "CON":16, "INT":8, "WIS":12, "CHA":6}
    test_subject.set_stats(default_stats)
    assert test_subject.get_stats() == default_stats

def test_max_hp():
    assert test_subject.get_max_hp() == 71
    test_subject.set_max_hp("2")
    assert test_subject.get_max_hp() == 75

def test_get_character():
    assert test_subject.get_character() == {
        "Character Name" : "Simon",
        "Race" : "Elf",
        "Background" : "Beggar",
        "Alignment" : "CE",
        "Age" : "2",
        "Class" : "Cleric",
        "Subclass" : "Test",
        "Level" : 5,
        "STR" : 8,
        "DEX" : 8,
        "CON" : 8,
        "INT" : 8,
        "WIS" : 8,
        "CHA" : 8,
        "Max HP" : 75
    }


# These test the file saving, viewing, and editing functions:

def test_save_and_view_character():
    save_character(test_subject)
    # view character will fail if save character did not succeed
    view_character(test_subject.get_name())

def test_select_character(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    select_character("view")

def test_edit_character(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda : "quit")
    # This quits immediately. Other functions are tested independently
    edit_character(test_subject.get_name())

def test_delete_character():
    delete_character(test_subject.get_name())
    

# These test the "functions" module functions. Mostly about user input:

def test_input_in_given_range():
    # Checks limits of range, inside of range, out of range + or -, and string input
    assert check_input_within_given_range("4", -1, range(4)) == 3
    assert check_input_within_given_range("2", -1, range(4)) == 1
    assert check_input_within_given_range("1", -1, range(4)) == 0
    assert check_input_within_given_range("5", -1, range(4)) == "loop"
    assert check_input_within_given_range("0", -1, range(4)) == "loop"
    assert check_input_within_given_range("abc", -1, range(4)) == "loop"
    
def test_select_race(monkeypatch):
    # Makes "3" the default value for input()
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert select_race("Dave") == "Orc"

def test_select_background(monkeypatch):
    # Makes "3" the default value for input()
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert select_background("Dave") == "Wild Child"

def test_select_class(monkeypatch):
    # Makes "3" the default value for input()
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert select_class("Dave") == "Cleric"

def test_select_subclass(monkeypatch):
    # Makes "3" the default value for input()
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert select_subclass("Dave", 6, "Cleric") == "Light Domain"
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert select_subclass("Dave", 6, "Cleric") == "Knowledge Domain"
    monkeypatch.setattr('builtins.input', lambda _: "7")
    assert select_subclass("Dave", 6, "Cleric") == "War Domain"



def test_increase_to_level(monkeypatch):
    # Makes "2" the default value for input(). 
    # Here, it selects "average" for hp raise choice
    monkeypatch.setattr('builtins.input', lambda _: "2")
    # Checks that setting level to the same level doesn't cause changes
    assert increase_to_level(test_subject, 5) == 75
    # Raises the level by 1, to 6
    test_subject.set_level(6)
    # Checks that the max hp is raised by 1 level's worth: 4 pts
    assert increase_to_level(test_subject, 5) == 79


# Checks dice rolling feature 
def test_dice_roller():
    for i in range(2,1001):
        assert roll_die(1, i, 0) in range(1,i+1)
    for i in range(1,1001):
        assert roll_die(i, 20, 0) in range(i, 20*i+1)


