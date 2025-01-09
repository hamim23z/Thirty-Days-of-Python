"""
There are four different collection data types in Python. 
    • List: a collection of ordered and changeable information. It can have duplicate members. 
    • Tuple: a collection or ordered and unchangeable information. It can have duplicate memebers. 
    • Set: a collection of unordered, unindexed, and unchangeable information. But we can add new items to the set. It cannot have duplicate members. 
    • Dictionary: a collection of unordered, changeable, and indexed information. It cannot have duplicate members. 
"""



"""
How to Create a List:
    • The first method is by using the list built in function. We can do it by
    doing: 
    new_list = list() #this is an empty list
    empty_list = list() #this is an empty list

    
    • The second method is by using square brackets. This is the way I do, seems
    easier:
    new_list = []
    empty_list = []
"""



"""
Lists with Values and Finding Length
    • Similar to finding the length of a string, we do the same thing for finding 
    the length of a list. 
    fruits = ['banana', 'orange', 'mango', 'lemon']
    how_many_fruits = print(len(fruits))


    • Lists can have items of different data types. They don't all have to be
    strings, integers, floats, etc. 
    random_list = ["Hamim", 20, 3.14, True, "Yolo"]
"""



"""
Accessing List Items using Positive and Negative Indexing
    • Just like a string, to find the first value, last value, or any value, 
    we use the index. It starts at index 0 as always. 

    • To find the first index we do. We can also use negative index. It would be -4 here.
    fruits = ['banana', 'orange', 'mango', 'lemon']
    first_fruit = fruits[0]
    print(first_fruit) #banana


    • To find the last index there are two different ways to do it, the negative index or use
    the length method. 

    • This is the length method
    fruits = ['banana', 'orange', 'mango', 'lemon']
    last_fruit = len(fruits) - 1
    print(last_fruit)

    • This is the negative index method
    last_fruit = fruits[-1]
    print(last_fruit)
"""



"""
Unpacking List Items
    • If we have a list, we can individually pull out the elements inside the list. And if it is too big,
    we can use *rest which is sort of like a skip, but it still outputs it. 

    first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
    print(first)          # 1
    print(second)         # 2
    print(third)          # 3
    print(rest)           # [4,5,6,7,8,9]
    print(tenth)          # 10
"""



"""
Slicing Items From a List
    • Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, 
    the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)

    fruits = ['banana', 'orange', 'mango', 'lemon']

    • To get the value of all the fruits, we can do 
    all_fruits = fruits[0:4] #start at 0 and don't include value at index 4
    print(all_fruits)
    all_fruits = fruits[0:]
    print(all_fruits)
    all_fruits = fruits[-4:]
    print(all_fruits)

    • To get the value of some of the fruits, say orange and mango
    some_fruits = fruits[1:3] #start at 1 and don't include value at index 3
    print(some_fruits)
    orange_and_mango = fruits[-3:-1]
    print(orange_and_mango)


    • To get the value of some of the fruits, using step
    orange_and_lemon = fruits[::2]
    print(orange_and_lemon)

    • This is a special case where it just takes the list in reverse order. So it will
    now become lemon, mango, orange, banana 
    reverse_fruits = fruits[::-1]
"""



"""
Modifying Lists
    • Since lists are modifiable we can modify the lists that we have
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits[0] = 'avocado'
    print(fruits) #['avocado', 'orange', 'mango', 'lemon']
"""



"""
Checking Items in a List
    • To check if a certain item is in the list, we can use the 'in' operator that Python has.
    fruits = ['banana', 'orange', 'mango', 'lemon']
    does_exist = 'banana' in fruits
    print(does_exist) #True

    does_exist2 = "Strawberry" in fruits
    print(does_exist2) #False
"""



"""
Adding Items in a List
    • To add an item to the list, we use the append() method. This adds it to the end of the list
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.append("apple")
    print(fruits) #['banana', 'orange', 'mango', 'lemon', 'apple']
"""



"""
Inserting Items in a List
    • We can use insert() method to insert a single item at a specified index in a list. 
    The insert() methods takes two arguments:index and an item to insert.
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.insert(2, 'apple')
    print(fruits) #['banana', 'orange', 'apple', 'mango', 'lemon']
"""


"""
Removing Items From a List
    • We can use the remove() method to remove an item from a list.
    fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
    fruits.remove('banana')
    print(fruits)  #['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list


    • The pop() method removes the specified index, (or the last item if index is not specified):
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.pop()
    print(fruits)  #['banana', 'orange', 'mango']

    fruits.pop(0)
    print(fruits)  #['orange', 'mango']


    • The del keyword removes the specified index and it can also be used to delete items within index range. 
    It can also delete the list completely
    fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
    del fruits[0]
    print(fruits)  #['orange', 'mango', 'lemon', 'kiwi', 'lime']
"""



"""
Clearing List Items
    • The clear() method just empties the list
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.clear()
    print(fruits) #[]
"""



"""
Copying a List
    • If we want to copy a list and its values within, we can just use the copy() method
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits_copy = fruits.copy()
    print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
"""



"""
Joining Lists
    • Similar to strings, we can join lists. There are different ways to do it. The first
    way to do it is the + operator
    positive_numbers = [1, 2, 3, 4, 5]
    zero = [0]
    negative_numbers = [-5,-4,-3,-2,-1]
    integers = negative_numbers + zero + positive_numbers
    print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    
    • The second way to do it is by using the extend() method
    num1 = [0, 1, 2, 3]
    num2= [4, 5, 6]
    num1.extend(num2)
    print(num1) #[0, 1, 2, 3, 4, 5, 6]
"""



"""
Counting Items in a List
    • The count() method returns the number of items an item appears in a list
    ages = [22, 19, 24, 25, 26, 24, 25, 24]
    print(ages.count(24)) #3
"""



"""
Finding Index of an Item
    • The index() method returns the index of an item in the list
    ages = [22, 19, 24, 25, 26, 24, 25, 24]
    print(ages.index(24))  #2, the first occurrence
"""



"""
Reversing a List
    • The reverse() method just reverses the order of the items in the list
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.reverse()
    print(fruits) # ['lemon', 'mango', 'orange', 'banana']
"""



"""
Sorting List Items
    • The sort() method reorders the list items in ascending order and modifies the original list. 
    If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.sort()
    print(fruits)  #sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']

    fruits.sort(reverse=True)
    print(fruits) #['orange', 'mango', 'lemon', 'banana']


    • The sorted() method returns the ordered list without modifying the original list
    fruits = ['banana', 'orange', 'mango', 'lemon']
    print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
    
    # Reverse order
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits = sorted(fruits,reverse=True)
    print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
"""