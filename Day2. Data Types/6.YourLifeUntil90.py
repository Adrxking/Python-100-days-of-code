# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# Get the age of the user
age = int(input("Write your age here...\n"))

years_remaining = 90 - age
days_remaining = 365 * years_remaining
weeks_remaining = 52 * years_remaining
months_remaining = 12 * years_remaining

print(f"You have {days_remaining} days remaining, {weeks_remaining} weeks remaining and {months_remaining} months remaining")