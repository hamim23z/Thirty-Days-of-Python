"""
Built In Function
    • In Python, there are a lot of built in functions. These functions are available globally and this means that
    we can make use of the built in functions without importing anything. 

    • Some of the most common functions are print(), len(), type(), int(), input(). These are just some of the many
    available. A quick Google search will show all of them. 
"""



"""
Variables
    • Variables store data in a computer memory. There are some unwritten rules when declaring a variable. We do not use 
    a number at the beginning, a special character, and a hyphen is not allowed either. Secondly, a variable can have a 
    short name but it is not recommended. 

    • For Python, some basic rules when declaraing a variable is that a variable must start with a letter or an underscore. 
    It cannot start with a number and must contain alphanumeric characters only. 

    • It is also important to note that variable names are case sensitive. 

    • We use snake_case variable naming convention. This means that after each word, we use an underscore. So a variable called
    firstname is wrong and first_name is correct. 

print("Hello world")
print(len("Hello, World!))
print("My First Name is:", first_name)
"""



"""
Declaring Multiple Variables in a Line
    • Multiple variables can also be declared in one line

first_name, last_name, age = "Hamim", "Choudhury", 20
"""



"""
Getting User Input
    • We use the built-in input function to get input from the user
   
location = input("Where are you right now?: ")
print(location)
"""



"""
Data Types
    • There are a lot of different data types in Python. And to identify the data type, we use the builtin type function. 

first_name = "Hamim"
age = 20
print(type(first_name))
print(type(age))
"""



"""
Casting
    • Casting means converting one data type to another data type. We use the builtin functions of int(), float(), and str()
    to cast. 
"""



"""
Integer to Float

number_int = 10
number_float = float(number_int)
print(number_float)
"""



"""
Float to Integer

gravity = 9.81
print(int(gravity))
"""



"""
Integer to String

number_int = 10
number_string = str(number_int)
print(number_string) 
"""



"""
String to Integer or Float

num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))
num_int = int(num_float)
print('num_int', int(num_int))
"""



"""
String to List

first_name = 'Hamim'
first_name_to_list = list(first_name)
print(first_name_to_list) ['H', 'A', 'M', 'I', 'M']
"""