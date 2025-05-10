# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("pou")
define n = Character("...")

# The game starts here.

label start:
    
    scene dark room

    n "The surrounding area is enveloped by a murky darkness, unpenetrated not even by the solace of a familiar sunlight that may have once shone through."
 
    n "A figure can be barely made out despite the unrelenting emptiness, the shape resembles something familiar yet strange at the same time. A triangular shape."


    scene bg room

   

    show pou:
     xalign 0.5
     yalign 0.5

    # These display lines of dialogue.

    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
