```
**Day 01 Quiz - Testing Knowledge and Syntax**

1. Comments
    -> There are two different types of comments, single line and multiline. Single is # and multiline is ''' or """


2. Data Types
    -> The different data types in Python are strings, numbers, floats, int, complex, boolean. More complex ones are lists,
      sets, tuples, and dictionaries.
      • In order to check what kind of data type it is, we can use the built in Python function type. So type(10) will
        return int.
```

<br>
<br>

```
**Day 02 Quiz - Testing Knowledge and Syntax**

1. Integer to Float
    random = 4
    new_float = float(random)
    print(new_float)


2. Float to Integer
    random2 = 3.14
    new_int = int(random2)
    print(new_int)


3. Integer to String
    random3 = 21
    new_string = str(random3)
    print(new_string)

And the other way is the same for them, just change the functions and whatnot. 
```

<br>
<br>

```
**Day 03 Quiz - Testing Knowledge and Syntax**

1. Boolean Operators
    -> In Python, we have True and False.


2. Assignment Operators
    -> == means equal to
    -> != means not equal to
    -> += means a = a+b
    -> -= means a = a-b
    -> *= means a = a*b
    -> /= means a = a/b
    -> %= means a = a%b


3. Comparison Operators
    -> > means greater than
    -> >= means greater than or equal to
    -> < means less than
    -> <= means less than or equal to


4. Logical Operators
    -> and. This evaluates to True when both expressions are True
    -> or. This evaluates to True when at least one expression is True.
    -> not. This reverses, so True becomes False and False becomes True.
```

<br>
<br>

```
**Day 04 Quiz - Testing Knowledge and Syntax**

1. Creating a String
    -> string = "Hello". Multiline strings also exist and can make them using ''' or """


2. String Concatenation
    -> There are two different ways to join strings. The first being a comma(,). When we do this, it automatically
        creates a space for us. The second way to create a string is by using the +, this doesn't make a space, so
        we have to do it ourselves.


3. Escape Sequences
    -> \n is new line
    -> \t is tab
    -> \\ is backslash
    -> \' is single quote. \" is double quote


4. String Interpolation
    -> print(f"{variable} is cool."). I like using this whenever I have multiple different variables.


5. Accessing Characters by Index
    -> We have a string called Python so then to get y we can do
    y_value = string[1]
    print(y_value)
    -> Negative indexing also exists, starts from -1


6. Slicing Strings
    -> We have a string called Python so then to get t and h we can do
    t_and_h = string[2:4]
    print(t_and_h)


7. Reversing a String
    -> We have a string called Python so then to reverse we can do
    reverse_this = string[::-1]
    print(reverse_this)


8. Capitalize
    -> print(string.capitalize())
    -> What this does it capitalize the string aka the first letter


9. Count
    -> print(string.count('y'))
    -> What this does is count the number of occurrences something occurs in the string.


10. EndsWith
    -> print(string.endswith('z'))
    -> What this does is checks if the string ends with what the user entered in the (). Returns True or False


11. Expand Tabs
    -> print(string.expandtabs(100))
    -> What this does is expand the tabs, simple


12. Find
    -> print(string.find("Hello"))
    -> What this does it that it looks for what the user entered in the (). Returns the first index of it.
    -> If not found, -1


13. rFind
    -> print(string.rfind("Hello"))
    -> What this does it that it looks for what the user entered in the (). Returns the last index of it.
    -> If not found, -1


14. isalnum
    -> print(string.isalnum())
    -> What this does is check if the string is alpha numerical. Returns True or False.


15. isalpha
    -> print(string.isalpha())
    -> What this does is check if the string is alphabet characters. Returns True or False.


16. isdecimal
    -> print(string.isdecimal())
    -> What this does is check if the string has all decimal values in it. Returns True or False.


17. isdigit
    -> print(string.isdigit())
    -> What this does is check if the string has all digits. Returns True or False.


18. isnumeric
    -> print(string.isnumeric())
    -> What this does is check if the string is numerical. Returns True or False. 


19. islower and isupper
    -> print(string.islower()) or print(string.isupper())
    -> What this does is check if the string is uppercase or lowercase. Returns True or False.


20. Replace
    -> print(string.replace("Python" , "Javascript"))
    -> Replaces something
```
