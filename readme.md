# DnD 5e Character Creator + Dice Roller
## JackDixon_T1A3

### <u>Source Control Repository</u>
[Link to Github](https://github.com/JackDixon019/T1A3_DnD_Character_Creator)

### <u>Presentation</u>
[Link to presentation](https://youtu.be/fO7vDJvicT4)

### <u>Software Development Plan</u>
DnD 5e Character Creator is a CLI tool to assist users in creating, saving, and editing character-sheets for the tabletop RPG Dungeons and Dragons 5th edition. This tool is aimed at people familiar with DnD, and is at present *technically* incomplete. 

Still needed to be added are a full race and background list, as well as proficiencies. Although these features are currently missing or lacking, the core features of the program are functioning.

#### Features

1. Character Creator
    - This is the core feature of the program. 
    - Includes:
        - Assigning Stats
        - Levels
        - Class selection
    - Characters are saved as a file
2. Character Editor and Viewer
    - Allows viewing and editing of character files
3. Dice Roller
    - This was needed as part of the character creator, so I expanded it to be a standalone feature as well.

### <u>Installation and Use</u>
To install the app, run the ```install-and-run.sh``` script. This can be done through the a CLI with the command:
```
source run.sh
```

This will create and open a virtual environment, before installing dependencies and finally, running the program.

From there, the menu can be navigated via typing numbers that correspond to numbered lists. for example, the main menu is comprised of:
```
1. Create a character
2. View a character
3. Edit a character
4. Delete a character
5. Roll some dice
6. Exit
```
When the user types ```1``` they begin creating a new character. The following menus guide the user through the process of character creation by either prompting the user for input, such as when asking the user for a name for their character, or providing a numbered list of options.

In cases where the user inputs an invalid input, such as a string in a numbered list or a number outside of the allowed range, the user will be prompted to enter a value from within the allowable range.

Listed options are coloured in a salmon-pink colour, while prompts are coloured green. Variable numbers, such as rolled scores or point-buy stats, and character information, are in yellow. Finally, error messages are in red. 

The exception to this numbered-list method of navigation is in the selection of stats to assign scores:

```
Please enter a stat you would like to assign the score: {score}

STR
DEX
CON
INT
WIS
CHA
```

In this section of the app, users must type their chosen stat, such as ```STR```. This menu is case-insensitive; ```str``` or ```Str``` will also work.

In the menus where the user must type their desired stat, typing anything not in the list of stats, or a stat that already has a score assigned to it, the app will prompt the user to enter a stat from the list. 

##### Dependencies
This program requires ```Python 3.10``` or later, due to the use of Match-Case statements. Python can be obtained <u>[from the Python website.](https://www.python.org/downloads/)</u>

This program is dependent on the package ```Colored 1.4.4```. This is installed when using the ```install-and-run``` script, but <u>[can also be accessed from the Colored website.](https://pypi.org/project/colored/)</u>

Not required to run the program itself, but used for testing, is the Pytest package, <u>[available from the Pytest website](https://docs.pytest.org/en/7.3.x/getting-started.html#get-started)</u>



### <u>Implementation Plan</u>
##### Character Creation
The character creation feature is the primary feature of the app. No internet connection is required for use. Data for the character creation options is obtained from the libraries.py file. Currently, the race and backgrounds lists are unfinished, however the class and subclass lists contain all classes and subclasses from the base-edition of DnD 5e. 

###### Checklist
- Create Character class | Priority: High
    - Contains character info: 
        - Name
        - Age
        - Alignment
        - Background
        - Race
        - Class
        - Subclass
        - Level
        - Max HP
        - Ability Scores
    - Deadline: 25/04
- Assign misc. character details | Priority: Medium
    - Includes non-restricted data entry
        - Name
        - Age
        - Alignment
    - Deadline: 26/04
- Assign Character level | Priority: High
    - Level is restricted between 1 and 20
    - Deadline: 26/04
- Assign Character's class | Priority: High
    - Classes to be taken from base edition of DnD 5e:
        - Barbarian
        - Bard
        - Cleric
        - Druid
        - Fighter
        - Monk
        - Paladin
        - Ranger
        - Rogue
        - Sorcerer
        - Warlock
        - Wizard
    - Subclasses also taken from base edition DnD 5e. 
    - Deadline: 27/04
- Assign character stats | Priority: Medium
    - Stats assigned in 3 ways:
        1. Point-buy
            - User has 27 points to spend
            - All stats start at 8
            - No stats can exceed 15
        2. Roll 4d6, pick 3
            - User rolls 4x 6-sided die
            - Highest 3 rolls are chosen
            - Stats are assigned after 6 scores are calculated
        3. Roll 3d6
            - User rolls 3x 6-sided die
            - Stats are assigned after 6 scores are calculated
    - Deadline: 29/04
- Determine character Max HP | Priority: Low
    - Determined on a per-level basis
    - Calculated in one of two ways:
        1. User rolls class-specific hit-die and then adds CON modifier: (CON-10/2)
        2. Average of class-specific hit-die is used instead of rolling
    - Deadline: 02/05

##### File Viewing & Editing
The file viewing and editing features allow the user to view and edit saved character sheets. Character sheets are written and read by the csv module built-into python, and can be viewed or edited in the app. 

###### Checklist
- Save files | Priority: High
    - Deadline: 03/05
- Check files | Priority: Medium
    - Deadline: 03/05
- View files | Priority: High
    - Deadline: 04/05
- Edit files | Priority: Medium
    - Deadline: 05/05
- Delete files | Priority: Low
    - Deadline: 05/05

##### Dice Roller
The dice roller is used in the character-creation feature, and can also be used independently to roll whatever combination of dice desired. If the user rolls 2d20, the Dice Roller will ask the user whether they are rolling with Advantage or Disadvantage. Advantage and Disadvantage are features of DnD, where the user rolls 2d20 and then selects either the higher or lower value respectively. I utilise the Advantage condition when rolling 4d6 (pick 3) to determine stats, allowing me to use the dice-rolling function to fill this purpose as well. 

###### Checklist
- Get dice | Priority: Medium
    - Deadline: 01/05
- Check Advantage | Priority: Low
    - Deadline: 01/05
- Roll Dice | Priority: High
    - Deadline: 29/04
- Return sum of rolls | Priority: High
    - Deadline: 29/04

#### Testing
Testing was primarily performed using the ```pytest version 7.3.1``` testing suite. Functions that required one or no user inputs were tested automatically using pytest, but for testing features such as error-handling, menu navigation, and colour of text, manual testing was used. Manual testing was also used for features that required several user inputs to function, such as the create_character() function, and for testing ```while``` loops.

Testing for this program was performed on the MacOS Ventura operating system. 