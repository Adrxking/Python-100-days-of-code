
# Give welcome to the program
print("Welcome to the tip calculator")

# Ask user for bill total
total = int(input("What was the total bill? "))

# Ask user for percentage tip he would like to give. Must be 10, 12 or 15
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# Ask user for people to split the bill
split = int(input("How many people to split the bill? "))

total_with_tip = total * (1 + tip / 100)

total_per_person = round(total_with_tip / split, 2)
total_per_person = "{:.2f}".format(total_per_person)

print(f"Each person has to pay {total_per_person}€")
