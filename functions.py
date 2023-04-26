from character import Character


def create_character():
    # Creates character with default statline and no details
    current_character = Character("", "", "None chosen", "None chosen", "None chosen", "None chosen", 0, "No subclass chosen (yet)", 1, 8, 8, 8, 8, 8, 8, 0)

    # Name
    current_character.set_name()
    
    # Race
    current_character.set_race()

    # Background
    current_character.set_background()

    # Alignment
    current_character.set_alignment()

    # Age
    current_character.set_age()

    # Level
    current_character.set_level()
    
    # Class
    current_character.set_character_class()

    # Subclass
    current_character.set_subclass()

    # Stats
    current_character.set_stats()
                
    # Create character
    return current_character