## 1. Age Group Categorization
# - Classify a person's age Group: Child (<13), 
# Teenager (13-19), Adult(20-59), Senior (60+).

age = input("Please enter your age: /n")

age_in_int = int(age)

# Conditional Logic
if age_in_int < 13:
    print("Child")

elif age_in_int < 20:
    print("Teneeger")
elif age_in_int < 60:
    print("Adult")
else:
    print("Senior")