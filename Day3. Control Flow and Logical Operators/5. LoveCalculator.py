##############################################
#######---- PIZZA ORDER EXERCISE -----########
##############################################
# Questions
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


# Combine the names
combined_string = name1 + name2

# Transfor to lowercase
lower_case_string = combined_string.lower()

# Count how many times the letters repeates
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

# Get the number of all repeats
true = t + r + u + e

# Count how many times the letters repeates
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

# Get the number of all repeats
love = l + o + v + e

# Combine both repetitions
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos." )
elif (love_score >= 40) and ( love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")  
else:
    print(f"Your love score is {love_score}, you are alright together.")  
    