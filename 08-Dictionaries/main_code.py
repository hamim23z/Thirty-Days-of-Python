"""
Level One Exercises are Below
"""

#Number One
dog = {}


#Number Two
dog['name'] = 'Bartholemew'
dog['color'] = 'Brown'
dog['legs'] = 4
dog['age'] = 2
print(dog)


#Number Three
student = {
    'first_name' : 'Austin',
    'last_name' : 'Reaves',
    'gender' : 'Male',
    'status' : 'Single',
    'skills': ['HTML', 'CSS', 'JS', 'Python'],
    'city' : 'New Jersey',
    'address' : 'Homeless'
}


#Number Four
print(len(student))


#Number Five
print(student['skills'])


#Number Six
student['skills'].append("HTML")
print(student)


#Number Seven
print(student.keys())


#Number Eight
print(student.values())


#Number Nine
print(student.items())


#Number Ten
student.popitem()
print(student)


#Number Eleven
del dog