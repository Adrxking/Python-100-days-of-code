# Convert an Integer into String
print( "The number of characters of your name is -> " + str( len( input("Write your name -> \n") ) ) )

# Convert a String into a Float
print(123 + float("123.123"))

# Program that adds the digits in a 2 digit number.
#e.g. If the input is 35 then we have to do 3 + 5 = 8
both_digits = input("Please write two digits\n")

first_digit = int(both_digits[0])
second_digit = int(both_digits[1])

print("The result of " + str(first_digit) + " + " + str(second_digit) + " is " + str(first_digit + second_digit) )