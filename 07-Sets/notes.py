"""
Sets
    • A set is a collection of items. They are unordered and unindexed distinct items.
    It is used to store unique items. 
"""



"""
Creating a Set
    • There is only one way to create a set, we can do. We must include the set keyword
    empty_set = set()
"""



"""
Set With Values
    fruits = {"apple", "banana", "orange", "strawberry"}
"""



"""
Getting The Length of a Set
    • We use the len() function once again to find it
    print(len(fruit))
"""



"""
Accessing Items in a Set
    • In order to access items in a set, we need to use a loop which will be covered later. 
"""



"""
Checking if Item Exists
    • We use the "in" operator once again for it
    does_exist = "strawberry" in fruits
    print(does_exist) #True
"""



"""
Adding Items to a Set
    • Once we make a set, we cannot change any items but we can add more items. When we use add()
    it only allows us to add ONE item
    fruits = {"apple", "banana", "orange", "strawberry"}
    fruits.add("watermelon")

    • If we use update(), then it will allow us to use multiple items to the set but the syntax is
    a little bit different from add
    fruits = {"apple", "banana", "orange", "strawberry"}
    fruits.update(["blackberry", "cherry", "peach"])
"""



"""
Removing Items From a Set
    • We can remove an item using remove() but if the item we want to remove does not exist, then it 
    will cause errors.
    fruits.remove("peach")

    • If we use pop(), then it will remove a random item sfrom the list and returns the removed item
    fruits.pop()
"""



"""
Clearing Items From a Set
    • Just like before, to clear a set, we can use the clear() method
    fruits.clear()
    print(fruits) # set()
"""



"""
Deleting a Set
    • If we want to delete the set completely and not just clear it, we use the del operator
    del fruits
"""



"""
Converting List to Set
    • We can convert a list to set or a set to a list. If we convert a list to a set, then it removes
    the duplicate items if they exist. 
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]
    convert_to_set = set(my_list)
    print(convert_to_set)
"""



"""
Joining Sets
    • If we want to join two sets, we can use the union() or update() method
    set1 = {1, 2, 3, 4, 5}
    set2 = {6, 7, 8, 9, 10}
    set3 = set1.union(set2)
    print(set3)

    set1 = {1, 2, 3, 4, 5}
    set2 = {6, 7, 8, 9, 10}
    set1.update(set2)
    print(set1)
"""



"""
Finding Intersection Items
    • Intersection items means finding items that exist in both sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {5, 6, 7, 8, 9, 10}
    intersection = set1.intersection(set2)
    print(intersection)
"""



"""
Checking Subset and SuperSet
    • To check if it's a subset, we use issubset() and for superset we use issuperset()
    whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even_numbers = {0, 2, 4, 6, 8, 10}
    whole_numbers.issubset(even_numbers) # False, because it is a super set
    whole_numbers.issuperset(even_numbers) # True
"""



"""
Checking the Difference Between Two Sets
    • We use the difference() to find the difference between two sets
    whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even_numbers = {0, 2, 4, 6, 8, 10}
    whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
"""



"""
Finding Symmetric Difference Between Two Sets
    • It returns the symmetric difference between two sets. It means that it returns a set that contains 
    all items from both sets, except items that are present in both sets, mathematically: (A\B) U (B\A)
    whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    some_numbers = {1, 2, 3, 4, 5}
    whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}
"""



"""
Joining Sets
    • If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are 
    joint or disjoint using isdisjoint() method.
    even_numbers = {0, 2, 4 ,6, 8}
    odd_numbers = {1, 3, 5, 7, 9}
    even_numbers.isdisjoint(odd_numbers) # True, because no common item
"""