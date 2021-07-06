# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = int(age) * 365
weeks = int(age) * 52
months = int(age) * 12

days_left = 90 * 365 - days
weeks_left = 90 * 52 - weeks
months_left = 90 * 12 - months

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

# age_as_int = int(age)
# years_remaining = 90 - age_as_int

# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
# print(message)