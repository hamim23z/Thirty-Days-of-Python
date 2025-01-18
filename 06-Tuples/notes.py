"""
Tuple
    • A tuple is a collection of different data types which is ordered and unchangeable. 
    They are created by using parenthesis (). Once it is created, we cannot change its
    values or do any modifications to it. 
"""



"""
Creating a Tuple:
    • An empty tuple can be made by doing:
    empty_tuple = () 
    empty_tuple = tuple()
"""



"""
Tuple with Values:
    • In order to put values in the tuple, it's just like a list.
    new_tuple = ("Hamim", "Hello", "How", "Are", "You")
"""



"""
Length of a Tuple:
    • Just like a list, to find the length of a tuple we use len()
    print(len(new_tuple))
"""



"""
Accessing Tuple Items:
    • Similar to a list, to find a certain item in a tuple we do:
    first_item = new_tuple[1]
    print(first_item) # Hamim

    • We can also use negative indexing to find items in a tuple
    second_to_last_item = new_tuple[-2]
    print(second_to_last_item)
"""



"""
Slicing Tuples:
    • We can slice out items from a tuple using the same format that we have been
    hello_and_how = new_tuple[1:3]
    print(hello_and_how)
"""



"""
Changing Tuples to a List:
    • We can change tuples to lists and lists to tuples. If we ever wanted to modify a tuple
    we should convert it to a list
    convert_to_list = list(new_tuple)

    • If we had a list, and wanted to convert it we could do
    number_list = [1, 2, 3, 45]
    convert_to_tuple = tuple(number_list)
"""



"""
Checking Item in a Tuple:
    • We use "in" to see if an item exists in a tuple. And then it'll return True or False
    names = ("Hamim", "John", "George")
    does_exist = "Matthew" in names
    print(does_exist)
"""



"""
Joining Tuples:
    • We can join two or more tuples by using the + operator
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (6, 7, 8, 9, 10)
    tuple3 = tuple1 + tuple2
    print(tuple3)
"""



"""
Deleting Tuples:
    • We can't delete a single item from a tuple but we can delete the entire tuple itself
    del tuple1
    del tuple2
    del tuple3
"""