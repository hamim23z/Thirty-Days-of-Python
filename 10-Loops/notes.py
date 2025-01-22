"""
While Loops
    • The while loop needs the word "while" in it. It is used to execute a block of statements repeatedly
    until a given condition is satisfied. When the condition becomes false, loop stops
    while condition:
        code goes here

    • If we want to run a block of code once the condition is no longer true, we can use else
    while condition:
        code goes here
    else:
        code goes here
"""



"""
Break and Continue
    • We use break when we like to get out of or stop the loop.
    • We use break when we like to stop our loop before it is completed.
    while condition:
        code goes here
        if another_condition:
            break

    • We use continue when we want to skip the current iteration and continue with the next iteration
    • We use continue when we like to skip some of the steps in the iteration of the loop
    while condition:
        code goes here
        if another_another:
            continue        
"""



"""
For Loop
    • With the for loop, we need the for keyword. Loop is used for iterating over a sequence that can either be
    a list, a tuple, a dictionary, a set, or a string.

    • A for loop with a list
    for iterator in list:
        code goes here

    • A for loop with a string
    for iterator in string:
        code goes here

    • A for loop with a tuple
    for iterator in tuple:
        code goes here

    • A for loop with a dictionary
    for iterator in dictionary:
        code goes here

    • A for loop with a set
    for iterator in set:
        code goes here
"""



"""
The Range Function
    • The range() function is used as a list of numbers. The range takes three parameters. Starting, ending, and increment.
    By default, it starts from 0 and the increment is 1. It needs at least 1 argument always, which is the end. So it is like
    range(start, end, increment)
    lst = list(range(11)) 
    print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
    print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    for iterator in range(start, end, step)
"""



"""
Nested For Loops:
    • This is when there is a loop inside a loop.
    for x in y:
        for t in x:
            print(t)
"""



"""
For Else
    • We use this if we want to execute some message when the loop ends
    for iterator in range(start, end, increment):
        do something
    else:
        print("The loop ended)
"""



"""
Pass
    • When a statement is required after a semicoon but we don't want to execute any code there, we can write pass
    to avoid any errors. It's basically a placeholder for future statements as well. 
    for number in range(6):
        pass
"""