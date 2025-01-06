"""
Level One Exercises are Below
"""
#Number One
age = 20


#Number Two
height = 71.0


#Number Three
complex_number = 1+8j


#Number Four
a = int(input("Enter base: "))
b = int(input("Enter height: "))
print('The area of the triangle is', (a*b*0.5))


#Number Five
side_a = int(input("Enter side a:"))
side_b = int(input("Enter side b:"))
side_c = int(input("Enter side c:"))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)


#Number Six
length = int(input("Enter length:"))
width = int(input("Enter width:"))
area = length * width
perimeter2 = 2 * area
print("The area of the rectangle is", area)
print("The perimeter of the triangle is", perimeter2)


#Number Seven
radius = float(input("Enter radius of circle:"))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print("The area of the circle is", area)
print("The circumference of the circle is", circumference)


#Skipping 8, 9, 10, and 11


#Number Twelve
len('python') != len('dragon')


#Number Thirteen
if 'on' in 'python' and 'on' in 'dragon': #cannot do, if on in python and dragon. Need to check it separately. 
    print(True)
else:
    print(False)


#Number Fourteen
text = 'I hope this course is not full of jargon'
if 'jargon' in text:
    print(True)
else:
    print(False)


#Number Fifteen
drag = 'dragon'
pyth = 'python'
if 'on' in drag and 'on' in pyth:
    print(False)
else:
    print(True)


#Number Sixteen
lengthtext = len('python')
float_version = float(lengthtext)
string_version = str(float_version)
print(lengthtext)
print(float_version)
print(string_version)


#Number Seventeen
#Using Python, we can check if a number is even or not by using the modulus operator and if statements. If x % 2 ==0, then we
#know that it is even since remainder is 2. Else, it is odd. 


#Number Eighteen
print(7//3) #this equals to 2


#Number Nineteen
check1 = type('10')
check2 = type(10)
print(check1 == check2)


#Number Twenty
check3 = type(9.8)
check4 = type(10)
print(check3 == check4)


#Number Twenty One
hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate of pay per hour: "))
earning = hours*rate
print("Your weekly earning is", earning)


#Number Twenty Two
years = int(input("Enter number of years you have lived: "))
total_seconds = years * 31536000
print("You lived for a total of", total_seconds, "seconds")


#Number Twenty Three
#Will come back to this. 