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

    # These display lines of dialogue.

    e "{bt=10}Helloooooooo!~{/bt}"

    e "you're alone on this one."

    e "Also, it would be nice to make a folder and organize the rest of the shit with the scripts so we'll do that later, k?"

    e "prob some shit like, importing the scene in script to tell it to go fuck itself with another file in another folder instead of script.rpy..."

    e "idk, later lol"
    # This ends the game.

    return
