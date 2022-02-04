import random

##############################################
#########------- LONG METHOD -------##########
##############################################

# Ask for the names
names_string = input("Give me everybody's names, separated by a comma. ")

# Transform the input to an array of names
names = names_string.split(",")

# Get the number of names
length_names = len(names)

# Get the number of who will pay
random_choice = random.randint(0, length_names-1)

# Get the random name who will pay
person_to_pay = names[random_choice]

# Show who will pay
print(person_to_pay + " is going to pay today!")

##############################################
#########------- SHORT METHOD -------#########
##############################################
# Ask for the names
names_string = input("Give me everybody's names, separated by a comma. ")

# Transform the input to an array of names
names = names_string.split(",")

# Get the random choice
person_to_pay = random.choice(names)

# Show who will pay
print(person_to_pay + " is going to pay today!")
