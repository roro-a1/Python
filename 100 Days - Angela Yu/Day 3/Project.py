# Treasure Island.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to the Treasure Island!!")
print("Your mission is to save the princess, but you cannot defeat the 'Eternal' without the treasure")
fork = input("The princess needs you now, but the princess is on the 'left' and the treasure on the 'right'. Choose!!")
if fork == "left":
    print("Game Over!! You cannot fight 'Eternal' with your puny strength.")
elif fork == "right":
    print("You made right choice Hero. Now let's go, we need to reach Island before the twilight.")
    boat = input("To reach the Island you can either 'swim' or 'wait' for the boat. What will you choose now? ")
    if boat == "swim":
        print("Game Over!! This was the trap by 'Eternal'")
    elif boat == "wait":
        print("""
    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~


        
        """)
        print("Is this not an amazing view! You have got brain. You did not become the piranha dinner")

        weapon = input("This is your final choice!! What treasure do you want? A 'sword' to slay or a 'ring' to impress? ")
        if weapon == "ring":
            print("Game Over!! You cannot fight 'Eternal' with your puny strength. You needed that sword.")
        elif weapon == "sword":
            print("Congratulations Hero!! You won. 'Eternal' ran away. You can have your princess and the 'ring' is your gift")
        else:
            print("Game Over!! The bug ate your game")

    else:
        print("Game Over!! The bug ate your game")

else:
    print("Game Over!! The bug ate your game")


