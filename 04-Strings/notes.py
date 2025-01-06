"""
Strings
    • Text is a string data type. Any data type written as text is a string. Single, double, or
    triple quotes are strings. Can find the length of a string using the len() method. 
"""



"""
Multiline String
    • A multiple string can be created by using the triple single or triple double quote. 
"""



"""
String Concatenation
    • We can connect two different strings together. One of the most common way is by using the + operator. 
    When we use the + operator, it DOES NOT add a space, we need to do that ourselves. Another way to 
    concatenate strings is by using the , operator, it DOES add a space automatically. 
"""



"""
Escape Sequences
    • \n is new line. \t means tab, which is 8 spaces. \\ means backslash. \' means single quote. 
    \" means double quote. 
"""



"""
String Formatting
    • The % is not just modulus, it can be used to format a set of variables as well. It is important to note that
    %s means string. 
    %d means integers
    %f means floating point number
    %.number of digitsf means how many numbers you want after the decimal when formatting. %.3f means 3 numbers after decimal. 

    firstname = 'Hamim'
    lastname = 'Choudhury'
    formatted_string = 'My name is %s %s' %(firstname, lastname)


    • Another way to format is by using str.format
    firstname = "Hamim"
    lastname = "Choudhury"
    formatted_string = "My name is {} {}'.format(firstname, lastname)


    • And another way to format is by doing string interpolation. That is when our strings begin with f
    a = 10
    b = 33
    print(f'{a} + {b} = {a+b}')
"""



"""
Python Strings as Characters
    • We can unpack characters to better visualize this. 
    language = 'Python'
    a,b,c,d,e,f = language
    print(a) #p
    print(b) #y
    print(c) #t
    ...
    print(f) #n
"""



"""
Accessing Characters in Strings by Index
    • This is similar to unpacking characters but this time we use the index. Worth noting that we
    always start at index 0. 
    language = 'Python'
    first_letter = language[0] #P
    second_letter = language[1] #y

    last_index = len(language) - 1
    last_letter = language[last_index] #n #we typically do this when the string is too long, or else we can just count it


    • We can also start from the end and use negative index. Since there's no such thing as -0, we start from -1
    language = 'Python'
    last_letter = language[-1] #n
    secondlast_letter = language[-2] #o
"""



"""
Slicing Python Strings
    • We can slice strings into substrings. The syntax for doing so is string_name[starting index:go upto this index but do not include it]
    language = 'Python'
    first_three = language[0:3] #Pyt
    last_three = language[3:6] #hon

    
    • To find the last three or however many last, we don't have to include the number after the colon but we include the colon We could have just done 
    last_three = language[3:] 


    • It is also possible for us to skip characters when slicing. The syntaxt for this is somewhat complex as it takes three numbers. The first being
    the starting index. The second being the ending index. And thenn the third being the iteration. 
    language = 'Python'
    output = language[0:6:2] #Pto #so how this works is by starting at index 0, going upto index 6 and then incrementing by 2 and choosing the character there
"""



"""
Reversing a String
    • Reversing a string means exactly what it means and it is super simple to do. 
    language = 'Python'
    reversed = language[::-1]
    print(reversed) #nohtyP
"""



"""
String Methods
    • capitalize(): used to convert the first character of a string to a capital letter
    sentence = 'thirty days of python'
    print(sentence.capitalize()) #Thirty days of python


    • count(): used to return occurrences of the substring in the string
    sentence = 'thirty days of python'
    print(sentence.count('y')) #output is 3 bc there are 3 y's
    print(sentence.count('th')) #output is 2 bc there are 2 th's


    • endswith(): used to check if the string ends with what we are checking with
    sentence = 'thirty days of python'
    print(sentence.endswith('on')) #True
    print(sentence.endswith('yo')) #False


    • expandtabs(): replaces the tab character with spaces, the default tab size is 8. So it adds that many
    sentence = 'thirty\tdays\tof\tpython'
    print(sentence.expandtabs())   # 'thirty  days    of      python'


    • find(): returns the index of the first occurence of what we are searching for. if not found -1
    • It returns the lowest index of the substring if it is found. 
    sentence = 'thirty days of python'
    print(sentence.find('y')) #5


    • rfind(): returns the index of the last occurrence of what we are searching for. if not found -1
    sentence = 'thirty days of python'
    • It returns the highest index of the substring if it is found. 
    print(sentence.rfind('y')) #16


    • index(): returns the lowest index of a substring. if not found, gives valueError. 
    • It is like find() but gives a valueError if not found. 
    challenge = 'thirty days of python'
    sub_string = 'da'
    print(challenge.index(sub_string)) #7


    • rindex(): returns the highest index of a substring
    • It is like rfind() but gives a valueError if not found. 
    challenge = 'thirty days of python'
    sub_string = 'da'
    print(challenge.rindex(sub_string)) 


    • isalnum(): checks alphanumeric number
    • It basically has to have letters A-Z, a-z, OR numbers 0-9. 
    challenge = '30DaysPython'
    print(challenge.isalnum()) #True #bc it has letters and/or numbers

    challenge = 'thirty days of python'
    print(challenge.isalnum()) # False #bc space is not an alphanumeric character


    • isalpha(): checks if all string elements are alphabet characters. returns False otherwise
    challenge = 'ThirtyDaysPython'
    print(challenge.isalpha()) #True

    num = '123'
    print(num.isalpha()) #False 


    • isdecimal(): checks if all characters in a string are decimal 0-9
    • This is strictly for base 10 digits.
    challenge = '12 3'
    print(challenge.isdecimal())  # False #bc space not allowed


    • isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
    • This allows for more kinds of numerical symbols. 
    challenge = '\u00B2'
    print(challenge.isdigit()) #True


    • isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
    challenge = '30DaysOfPython'
    print(challenge.isidentifier()) # False, because it starts with a number


    • islower(): Checks if all alphabet characters in the string are lowercase
    challenge = 'thirty days of python'
    print(challenge.islower()) #True


    • isupper(): Checks if all alphabet characters in the string are uppercase
    challenge = 'THIRTY DAYS OF PYTHON'
    print(challenge.isupper()) #True


    • join(): Returns a concatenated string
    web_tech = ['HTML', 'CSS', 'Javascript', 'React', 'MUI']
    result = ' '.join(web_tech)
    print(result) #HTML CSS Javascript React MUI


    • strip(): Removes all given characters starting from the beginning and end of the string
    sentence = 'thirty days of python'
    print(sentence.strip('on')) #thirty days of pyth


    • replace(): replaces substring with a given string
    sentence = 'thirty days of python'
    print(sentence.replace('python', 'javascript')) #thirty days of javascript


    • split(): Splits the string, using given string or space as a separator
    challenge = 'thirty, days, of, python'
    print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']


    • title(): returns a title cased string
    sentence = 'thirty days of python'
    print(sentence.title()) #Thirty Days Of Python


    • swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
    challenge = 'Thirty Days Of Python'
    print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON


    • startswith(): checks if the string starts with the specified string
    challenge = 'thirty days of python'
    print(challenge.startswith('thirty')) #True
"""