import pytest
from character import Character
from libraries import default_stats


test_subject = Character("Dave", "Human", "Noble", "LG", "23", "Barbarian", "Path of the Totem Warrior", 6, 18, 13, 16, 8, 12, 6, 71)



def test_basic():
    assert "Hello" == "Hello"

def test_name():
   assert test_subject.get_name() == "Dave"
   assert test_subject.get_name() != "Simon"
   test_subject.set_name("Simon")
   assert test_subject.get_name() == "Simon"

def test_race():
    assert test_subject.get_race() == "Human"
    test_subject.set_race("Elf")
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


