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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenido a la isla del tesoro.")
print("Tu mision es encontrar el tesoro.")

choice1 = input("Estas en un cruce, donde eliges ir ? Escribe \"Izquierda\" o \"Derecha\" \n").lower()

if choice1 == "izquierda":
    choice2 = input("Has llegado a un lago. Hay una isla en medio del lago. Escribe \"esperar\" o \"nadar\" \n").lower()
    if choice2 == "esperar":
        choice3 = input("Has llegado a la isla desarmado. Hay una casa con 3 puertas. Una roja, una amarilla y una azul. Que color eliges? \n").lower()
        if choice3 == "roja":
            print("Has entrado en una habitacion en llamas. Game Over ;)")
        if choice3 == "amarilla":
            print("Has encontrado el tesoro!!!")
        if choice3 == "azul":
            print("Has entrado en una habitacion y te ha disparado el propietario. Game Over ;)")
        else:
            print("Esa puerta no existe.")
    else: 
         print("Te han comido entre 7 cocodrilos. Game Over ;)")
else:
    print("Te has caido en un agujero. Game Over ;)")