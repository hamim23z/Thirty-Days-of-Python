"""
Dictionary
    • A dictionary is a collection of unordered, modifiable paired by key:value data type.
"""



"""
Creating a Dictionary
    • To create a dictionary, we use curly braces or the dict() function but curly braces are
    the most common method.
    empty_dict = {}
"""



"""
Dictionary with Values
    • A dictionary can have any type of value, boolean, string, number, list, tuple, set, etc
    person = {
        'name': 'Hamim Choudhury',
        'age': 21,
        'location': 'NYC'
    }
"""



"""
Length of a Dictionary
    • To find the length of a dictionary, we can use the len() function again
    print(len(person))
"""



"""
Accessing Dictionary Items
    • To access items in the dictionary we can refer to its key name, remember that the format is key:value
    • Accessing an item by key raises an error if the key does not exist. But if we do not want this error
    then we can use the get method. This returns None if the key does not exist
    print(person['name'])
    print(person['age'])
    print(person.get('name'))
"""



"""
Adding Items to a Dictionary
    • Adding items to a dictionary is fairly simple
    person = {
        'name': 'Hamim Choudhury',
        'age': 21,
        'location': 'NYC'
    }
    person['school'] = 'CCNY'
    print(person)
"""



"""
Modifying Items in a Dictionary
    • We can modify items in a dictionary similar to the way we add items
    person['location'] = 'NYC Queens'
"""



"""
Checking Keys in a Dictionary
    • We use the in operator to see if a key exists in a dictionary
    does_exist = 'name' in person
    print(does_exist)
"""



"""
Removing Key and Value Pairs from a Dictionary
    • pop(key): removes the item with the specified key name
    • popitem(): removes the last item
    • del: removes an item with specified key name
    person = {
        'name': 'Hamim Choudhury',
        'age': 21,
        'location': 'NYC'
    }
    person.pop('name') #removes name and the value
    person.popitem() #removes location and the value
    del person['age'] #removes age and the value
    print(person)
"""



"""
Changing Dictionary to a List of Items
    • To change a dictionary to a list, we can use items(). This changes the dictionary to a 
    list of tuples
    print(person.items())
"""



"""
Clearing a Dictionary
    • If we don't want any of the items in a dictionary, we can clear using clear()
    print(person.clear())
"""



"""
Deleting a Dictionary
    • If we want to delete a dictionary completely, we use del
    del person
"""



"""
Copy a Dictionary
    • We can copy a dictionary using copy(). This allows us to avoid mutation of the original dictionary
    copy_of_person = person.copy()
    print(copy_of_person)
"""



"""
Getting Dictionary Keys as a List
    • The keys() method gives us the keys of a dictionary as a list
    print(person.keys())
"""



"""
Getting Dictionary Values as a List
    • The values() method gives us the values of a dictionary as a list
    print(person.values())
"""