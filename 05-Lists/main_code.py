"""
Level One Exercises are Below
"""

#Number One
empty_list = []


#Number Two
five_items = ["Hello", "This", "Is", "Five", "Items"]


#Number Three
print(len(five_items))


#Number Four
first_item = five_items[0]
middle_item = five_items[2]
last_item = five_items[-1]
print(first_item)
print(middle_item)
print(last_item)


#Number Five
mixed_data_types = ["Hamim", 21, "5 foot 11 inches", "Single", "NYC"]


#Number Six
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]


#Number Seven
print(it_companies)
print(mixed_data_types)


#Number Eight
print(len(it_companies))


#Number Nine
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]
print(first_company)
print(middle_company)
print(last_company)


#Number Ten
it_companies[0] = "META"
print(it_companies)


#Number Eleven
it_companies.append("NVIDIA")
print(it_companies)


#Number Twelve
it_companies.insert(3, "AMD")
print(it_companies)


#Number Thirteen
it_companies[1] = it_companies[1].upper()
print(it_companies)


#Number Fourteen
new_string = "#; "
it_companies.extend(new_string)
print(it_companies)


#Number Fifteen
checking = "Radeon" in it_companies
print(checking)


#Number Sixteen
it_companies.sort()
print(it_companies)


#Number Seventeen
it_companies.reverse()
print(it_companies)


#Number Eighteen
slice_first_three = it_companies[0:3]
print(slice_first_three)


#Number Nineteen
slice_last_three = it_companies[6:9]
print(slice_last_three)


#Number Twenty
slice_middle_three = it_companies[3:6]
print(slice_middle_three)


#Number Twenty One
it_companies.remove("Oracle")
print(it_companies)


#Number Twenty Two
it_companies.remove("IBM")
it_companies.remove("GOOGLE")
print(it_companies)


#Number Twenty Three
it_companies.remove("AMD")
print(it_companies)


#Number Twenty Four
it_companies.clear()
print(it_companies)


#Number Twenty Five
it_companies.clear()
print(it_companies)


#Number Twenty Six
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)


#Number Twenty Seven
full_stack.insert(5, "Python")
print(full_stack)
full_stack.insert(6, "SQL")
print(full_stack)





"""
Level Two Exercises are Below
"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Number One
ages.sort()
print(ages)


#Number Two
ages.append(19)
ages.append(26)
print(ages)


#Number Three
median = (24+24) // 2
print("The median age is:", median)


#Number Four
average = sum(ages) / len(ages)
print("The average age is:", average)


#Number Five
range = 26-19
print("The range of the ages is:", range)


#Number Six
calc1 = abs(19-22.75)
print(calc1)
calc2 = abs(26-22.75)
print(calc2)
print("The absolute value of min - average is greater than max - average")


#Not doing the last three involving countries