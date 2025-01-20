"""
Conditionals
    • Conditional execution is when a block of one or more statements will be executed if a certain 
    statement is true.
    • Repetitive execution is when a block of one or more statements will be repetitively executed as
    long as a certain expression is true.
"""



"""
If Condition
    • If something is true, then it will execute the block code and this will happen. The syntax is below. If 
    the condition is false, then we do not see the result.
    if condition:
        this part of the code runs only if the condition is True
"""



"""
If Else Condition
    • For the if statement above, I said that "if the condition is false then we do not see the result". But if
    we do want to see the result, then we use if else statements. The way it works is that if the condition is true,
    then it runs the block code for that. Else if it's not true (aka False), then it will execute the block code for
    else.
    if condition:
        this part of the code runs only if the condition is True
    else:
        this part of the code runs only if the condition is False
"""



"""
If Elif Else Condition
    • This essentially combines the if and if else conditional statements into one. When we want to have multiple if statements,
    we can't just do if if if if else. We need to use if elif elif elif ... else
    if condition:
        this part of the code runs only if the condition is True
    elif:
        this part of the code runs only if the first if was False and this is True
    else:
        this can be known as the default value or when everything else is False
"""



"""
Short Hand
    • If we want to save space and just want everything on one line we can use short hand syntax
    code if condition else code
"""



"""
Nested Conditions
    • Conditions can be nested. This means that if something is True, then go to the inner conditional statement and do something
    if condition:
        if condition:
            code goes here
        else:
            code goes here
    else:
        code goes here


    • We can avoid writing nested conditions by using the logical operator and or or
    if condition and condition:
        code

    if condition or condition:
        code
"""