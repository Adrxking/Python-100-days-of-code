##############################################
#######---- PIZZA ORDER EXERCISE -----########
##############################################
# Questions
print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L")
add_peperoni = input("Do you want peperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

# Set bill to 0
bill = 0

# Calculate the bill
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
if add_peperoni == "Y":
    if size == "S":
        bill += 2
    else :
        bill += 3
        
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is ${bill}")