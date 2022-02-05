# Get an array
student_scores = input("Input a list of student scores --> ").split(" ")

# Transform to int hole array
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

##############################################
#########------- SHORT METHOD -------#########
##############################################
higuest_score = max(student_scores)
print(f"The higuest score is: {higuest_score}")

##############################################
#########------- LONG METHOD -------##########
##############################################
higuest_score = None

for n in student_scores:
    if (higuest_score is None or n > higuest_score):
        higuest_score = n       

print(f"The higuest score is: {higuest_score}")
