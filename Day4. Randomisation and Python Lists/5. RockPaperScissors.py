import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("")
print("Bienvenido al juego de piedra, papel o tijera")
print("")
# Ask user for a choice
user_choice = int(input("Que eliges? Escribe 0 para Roca, 1 para Papel o 2 para Tijeras \n"))
if user_choice >= 3 or user_choice <0:
    print(f"{user_choice} no es una opcion valida, has perdido!")
    exit()
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
    
print(f"El ordenador elige:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("Has ganado!")
elif computer_choice == 0 and user_choice == 2:
    print("Has perdido!")
elif computer_choice > user_choice:
    print("Has perdido!")
elif computer_choice == user_choice:
    print("Empate!")
    