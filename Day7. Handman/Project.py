# Import packages
import random

# Create a word list
word_list = ["adrian","carmen","estefania"]
# Get one word from the word list
chosen_word = random.choice(word_list)
# Create an array with the selected word size and _ as values
user_word_builder = ["_" for _ in chosen_word]
# Set lives for the user
user_lives = 5
# Create a function that checks the letter the user set
def check_letter(user_letter):
    # Get the lives variable
    global user_lives
    correct_letter = 0
    for idx, _ in enumerate(chosen_word):
        if user_letter == chosen_word[idx]:
            print("Correcto!")
            correct_letter = 1
            user_word_builder[idx] = user_letter
    if correct_letter == 1:
        correct_letter = 0
        return None
    user_lives -= 1
    print("Incorrecto!, te quedan %d vidas" % user_lives)
    
# Create a function that show our current built word, ask the user for a letter and check the letter
def play():
    print(user_word_builder)
    user_letter = input("Please, write a letter\n")
    check_letter(user_letter)
    

# Create a loop while the word is not completed or the user has lifes to play
while ''.join(user_word_builder) != chosen_word and user_lives > 0:
    play()


print(user_word_builder)
print("GAME OVER!")