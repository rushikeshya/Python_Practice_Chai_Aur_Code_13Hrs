# 2. Movie Ticket Pricing
''' 
Problem:
- Movie tickets are priced based on age: 
- $12 for adults(18 and over), 
- $8 for children,
- Everyone gets a $2 discount on Wednesday 
'''

def ticket(age, weekday):
    ticket_price = 0
    if age < 18:
        ticket_price = 8
    elif age >= 18:
        ticket_price = 12

    # Apply discount if it's Wednesday (case insensitive)
    if weekday.lower() == 'wed':
        ticket_price -= 2
    return ticket_price

# Input Handling
row_age = input("Please Enter Your Age: ")
weekday = input("Please Enter Current Day:(sun, mon, tue, wed, thu, fri, sat) ")

try:
    # Convert age to integer
    age = int(row_age)
    # Calculate and display ticket price 
    print("Your Ticket prise is: $", ticket(age, weekday))
except:
    print("Invalid age input. Please enter a numeric value for age.")