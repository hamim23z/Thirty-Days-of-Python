"""
Level One Exercises are Below
"""

#Number One
for i in range(0,11):
    print(i)
print() #just to separate answers

i = 0
while i <= 10:
    print(i)
    i += 1
print() #just to separate answers


#Number Two
for i in range(10,-1,-1):
    print(i)
print() #just to separate answers

i = 10
while i >= 0:
    print(i)
    i -= 1
print() #just to separate answers


#Number Three
for i in range(1,8): #since we need to print 7 times, 1-7.
    print('#' * i) #this prints out the # and multiplies by i for how many in each row
print()


#Number Four
for i in range(1,9):
    for j in range(1,9):
        print('#', end='')
    print()
print() #just to separate answers


#Number Five
for i in range(0,11): #we see that it is 0-10, so we do 0,11 
    print(f'{i} x {i} = {i*i}')
print() #just to separate answers


#Number Six
languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in languages:
    print(language)


#Number Seven
for i in range(0,101):
    if (i%2 == 0):
        print(i)
print() #just to separate answers


#Number Eight
for i in range(0,101):
    if (i%2 != 0):
        print(i)
print() #just to separate answers





"""
Level Two Exercises are Below
"""

#Number One
sum = 0
for i in range(0,101):
    sum += i
print(f'The sum of all numbers is {sum}.')


#Number Two
sum_evens = 0
sum_odds = 0
for i in range(0,101):
    if (i%2 ==0):
        sum_evens += i
    else:
        sum_odds += i
print(f'The sum of evens is {sum_evens}. And the sum of odds is {sum_odds}.')





"""
Level Three Exercises are Below
"""
#Not doing any level exercises that ask for other files and folders that Asabeneh made. Skipping.