"""
Level One Exercises are Below
"""

#Number One
user_input = int(input("Enter your age: "))
if user_input >= 18:
    print("You are old enough to drive.")
else:
    print(f"You need {18-user_input} more years to learn to drive.")


#Number Two
my_age = 21
your_age = int(input("Enter your age: "))
if my_age > your_age: 
    print("I am older than you.")
elif your_age > my_age:
    print(f"You are {your_age - my_age} years older than me.")
else:
    print("We are the same age.")


#Number Three
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} and {b} are equal to each other")





"""
Level Two Exercises are Below
"""

#Number One
grade = int(input("Enter your grade: "))
if grade >= 80 and grade <=100:
    print("A")
elif grade >=70 and grade <=89:
    print("B")
elif grade >= 60 and grade <= 69:
    print("C")
elif grade >= 50 and grade <= 59:
    print("D")
elif grade >= 0 and grade <= 49:
    print("F")
else:
    print("Enter a valid grade from 0-100")


#Number Two
season = input("Enter a month to find season: ")
if season == 'September' or season == "October" or season == "November":
    print("The season is Autumn")
elif season == 'December' or season == 'January' or season == 'February':
    print("The season is Winter")
elif season == 'March' or season == 'April' or season == 'May':
    print("The season is Spring")
elif season == 'June' or season == 'July' or season == 'August':
    print("The season is Summer")
else:
    print("Enter a valid month and make sure the first letter is capitalized")


#Number Three
"""
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
my_fruit = 'mango'
if my_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(my_fruit)
    print(fruits)