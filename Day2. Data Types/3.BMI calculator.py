# BMI is the body mass index, BMI = Weight / height ** 2

# Ask for the height and weight. The height must be in meters
height = float(input("Enter your height...\n"))
weight = float(input("Enter your weight...\n"))

bmi = weight/(height**2)

print("Your BMI is " + str(bmi))