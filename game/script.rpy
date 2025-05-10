# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("pou")
define n = Character("...")

# The game starts here.

label start:
    
    scene dark room
    
    show dark room:
     xzoom 10
     yzoom 10

    n "The surrounding area is enveloped by a murky darkness, unpenetrated not even by the solace of a familiar sunlight that may have once shone through."
 
    n "A figure can be barely made out despite the unrelenting emptiness, the shape resembles something familiar yet strange at the same time. A triangular shape."

    n "Lights flash, all is clear, all that stands before is a singular entity, painted a sickly brown, surrounded by its own filth and staring at the source of this once absent light that now shone, a portrait of emptiness painted its face."

    n "Something that once knew love, something that once believed all their woes would disappear once that light appeared, but now, there laid a broken soul something that could not be mended."
    
    n "Start the game?"

    menu:
    
        "Start":
            jump choice1_yes
        
        "Close the game":
            jump choice2_no
        
            label choice1_yes:

            $ menu_flag = True
            n "Game starting..."
            jump choicestart_done
        
            label choice2_no:
            
            $menu_flag = False
            n "Game closing..."
            return
      
  
        
            label choicestart_done:   
    scene bg room

   

    show pou:
     xzoom 2
     yzoom 2               
     xalign 0.5
     yalign 0.5

    show white room behind pou:
        xzoom 10
        yzoom 10




    p "it’s you…"

    p "Long it has been since I had even dreamed of the crippling loneliness ending, I could not even entertain the very idea. Hope is something you must kill before it kills you"

    p "Why do you stare at me so, what is it you want from me?"

    p "Time as is my will, has been shattered, I know not the time I have been graced with the warming light of solidarity that I once took for granted"

    p "ANSWER ME OR LEAVE ME BE, WHY MUST YOU PROVOKE ME LIKE SOME KIND OF LOWLY ANIMAL, I DON’T WANT YOUR WORTHLESS PITY TO BE WASTED ON ME"

    n "Would you like to feed Pou or play a game?"
    menu:
    
        "Feed Pou":
            jump choice1_food
        
        "Play a game":
            jump choice2_game
        
            label choice1_food:

            $ menu_flag = True
            p "You wish to feed me?"
            p "Alas, it would be a lie were I to deny the divine taste of a corn on the cob or a humble artichoke, I suppose it would not be so troubling as to merely taste a morsel of what you have to offer?"
            menu:
                "refuse to give food":
                    jump choicefun_done
                
            jump choicefun_done
        
            label choice2_game:
            
            $menu_flag = False
            p "You wish… to play a game?"
            p "Long has it been since I last enjoyed the whimsy of a mere game. I had once missed these games of ours, though the passage of time has ravaged my memories, all that I forced to forget in order to survive this prison has now surfaced, like a festering wound I had ignored"
            menu:
                "refuse to play a game":
                    jump choicefun_done
            jump choice2_done
      
  
        
            label choicefun_done:
                p "Enough of these games! What do you want from me truly, if you expect me to lend you my trust once again, I’m afraid what trust I did have has surely been shattered by none other than you. You will find no forgiveness in my heart, there is NOTHING for you here... Leave."

                "hit him?"
                label choice4_decide:
            menu:
                "HIT HIM":
                    jump choice1_hit

                "Spare him...":
                    jump choice2_spare

            label choice1_hit:

            $ menu_flag = True  
            p "Why do you raise your fists at me? Have you not taken enough from me, stripped me of my dignity, left me to decay in a shrine of my own FILTH."
            p "Should you strike me, I solely ask that it is only strong enough so that you could finally end my suffering and free me of you once and for all."
           
            "Are you sure?"

            menu:
                "YES":
                    jump choice3_death
                "No...":
                    jump choice4_decide

            label choice3_death:
                n "As your strikes land unto pou, he becomes more and more bruised, and on its face lies not a face of contempt nor anger. In pou’s eyes all you see is pity towards you"
                show pou hurt: 
                    xalign 0.5
                    yalign 0.5
     

                p "Though my life may end, all I can feel within is a shearing sadness that while I am freed you must continue to live your worthless unremarkable life,"
                p "one of no recognition, no acknowledgement, in my final moments I am truly humbled that, despite my hardships, my life would not be nearly as pathetic as yours, and for that, I feel more sadness than I have in my entire life. I am truly sorry"
                "pou disappears"
                n "However, despite pou’s ramblings and pleas, all that escaped its mouth..."
                play sound "pou noise.mp3"
                n "was a simple sound…"
                "the end"
                return
            
            label choice2_spare:
            $ menu_flag = True
            p "A change of heart? I did not think it was possible, had I not abandoned hope my mind would have been spinning."
            p "However, despite all my attempts to crush my belief that things could be better, I could not help but feel my heart stir."
            p "After all this time I thought I had killed the hope left in me but I can feel a warm intent, a kindness I had long forgotten."
            p "Perhaps this time… things could be better between you and I."
            n "However, despite pou’s ramblings and pleas, all that escaped its mouth..."
            play sound "pou noise.mp3"
            n "was a simple sound…"
            "the end"

                


                
                


                    
                
                
    return
