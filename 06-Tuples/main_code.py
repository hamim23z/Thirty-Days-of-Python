"""
Level One Exercises are Below:
"""

#Number One
empty_tuple = ()


#Number Two
siblings = ("George", "John", "Chris", "Chandler")


#Number Three
brothers = ("George", "John", "Chris", "Chandler")
sisters = ("Ava", "Beatrice")
all_siblings = brothers + sisters


#Number Four
print(all_siblings)


#Number Five
family_members_list = list(all_siblings)
print(family_members_list)

family_members_list.append("Nolan")
family_members_list.append("Samantha")
print(family_members_list)

family_members_tuple = tuple(family_members_list)
print(family_members_tuple)





"""
Level Two Exercises are Below:
"""

#Number One
siblings2 = family_members_tuple[0:6]
parents2 = family_members_tuple[6:8]
print(siblings2)
print(parents2)


#Number Two
fruits = ("apple", "banana", "orange", "strawberry")
vegetables = ("carrot", "beetroot", "cucumber")
animal_products = ("milk", "fur", "eggs")
food_stuff_tp = fruits + vegetables + animal_products


#Number Three
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)


#Number Four
middle_items = food_stuff_lt[4:6]
print(middle_items)


#Number Five
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[7:10]
print(first_three)
print(last_three)


#Number Six
del food_stuff_tp


#Number Seven is skipped. Won't do anything countries related.