# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    show Andreas ph


    # call pronounselection 
    # disabled because malevolent is homophobic/j
    # charge ts somewhere else if we need more pronouns choice
    # btw, they them is default
    # there's also a ShowMenu("pronounselection") version for gui in the script

    # These display lines of dialogue.

    Andreas "wow"
    e "{bt=10}Helloooooooo!~{/bt}"

    # e "[they!t!c] with [pp!t] ??? holy shit woke you're alone on this one."

    e "it would be nice to make a folder and organize the rest of the shit with the scripts so we'll do that later, k?"

    e "prob some shit like, importing the scene in script to tell it to go fuck itself with another file in another folder instead of script.rpy..."

    e "idk, later lol"

    menu:
        e "What now?"

        "ze testin zon" :
            jump zetestinzon
        
        "test run":
            jump test
    return
