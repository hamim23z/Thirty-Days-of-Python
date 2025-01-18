"""
Level One Exercises are Below
"""

#Number One
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))


#Number Two
it_companies.add("Twitter")
print(it_companies)


#Number Three
it_companies.update(["Nvidia", "AMD", "Razor"])
print(it_companies)


#Number Four
it_companies.remove("AMD")
print(it_companies)


#Number Five
#What remove does is that it removes a specified item from the set. If it does not exist, it gives
#us an error. Discard does not give us any errors on the other hand.





"""
Level Two Exercises are Below
"""

#Number One
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
print(A)


#Number Two
intersection_finding = A.intersection(B)
print(intersection_finding)


#Number Three
subset_checking = A.issubset(B)
print(subset_checking)


#Number Four
disjoint_checking = A.isdisjoint(B)
print(disjoint_checking)


#Number Five
#Join A with B
B.update(A)
print(B)

#Join B with A
A.update(B)
print(A)


#Number Six
checking_symmetric = A.symmetric_difference(B)
print(checking_symmetric)


#Number Seven
del A
del B





"""
Level Three Exercises are Below
"""

#Number One
age = [22, 19, 24, 25, 26, 24, 25, 24]
convert_to_set = set(age)
print(convert_to_set)
print(len(age))
print(len(convert_to_set))
print("The length of the age aka age list is bigger bc it doesn't remove duplicates like sets.")


#Number Two
"""
So a string is a series of characters and they are enclosed in single quotes or double quotes.
A list is created by doing [], for empty and non empty sets. Different data types can be inside them and they can be modified. Can add or remove.
A tuple is created by doing (), for empty and non empty sets. Different data types can be inside and they cannot be modified. Cannot add or remove
A set is created by doing set() for empty and {} for values. They cant have different data types and cannot be modied. Can add or remove.
"""


#Number Three is skipped