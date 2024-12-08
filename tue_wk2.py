# Changing element positions

#first = input('Enter first number: ')
#second = input('Enter second number: ')
#print('Before swapping:', first, second)
#first = second
#second = first
#print('After swapping:', first, second)


# The below method works better to swap the positions of the numbers

first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)


top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)




# Python has methods to sort lists alphabetically 

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)



# Numbers can also be sorted from the lowest to the greatest

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

# to reverse the order you can use an argument

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)





# The Sort method is very hard to undo, so if you only want to temporarily sort a list and keep the original order you should use a general list function instead.

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)


# **REMEMBER** list_name.sort():      sorts the original list
#             sorted(list_name):      gives back a new, sorted list, keeps the original unchanged





# Checking Element Presence

for char in 'happy message':  # The above is used to check every element in a string
    print(char)
# The above can also be used to check every element in a list

invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited!')
    
    
# We can also reverse the code that will tell us True if the element is NOT found

invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')
    
    
    
    
    
# Copying lists

# Usually if we want to copy the variable, all we have to do is create a new variable and use the assignment operator
name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)

# The same rule for above does NOT apply for data collections like lists

list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

# The# name of the list is the memory location where the list is stored. Often called references because they reference other places in the memory
# Both variables now point to the very same place in the memory with the very same list and as a result when you try to modify some of the elements in one of the variables,
# You also modify the element of the other variable as well.


# to fix that we use slicing
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)


# If you want to copy the first 2 elements in the list you would use the below slicing
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)


# to create a new variable that point to the very same list we can do list 'New Equals' list
list_original = [1, 2, 3]
list_new = list_original
# So if you modify one of the above lists you'll also modify the other'





# List comprehension

# We use loops to make larger lists
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)
# The above will get the job done, but Python has list comprehension which creates larger lists faster


numbers = [i for i in range(1, 100)]
print(numbers)


numbers = [i for i in range(1, 100) if i % 3 != 0]
print(numbers)







# Nested Lists

# You can mix multiple data types with a single list, but it is not recommended
countries = [1, 'UK', 2, 'US']

# Lists can have other lists as elements
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3']]
print(cells[0]) # This will print out the first set ['A1', 'A2', 'A3']

# If you want to print out the first element of the first set
print(cells[0][0]) #This will print out A1

for x in cells:
    print('Element', x)
    
# For the individual elements, we use nested for loops
for x in cells:
    for y in x:
        print('Element', y)
        
# Nested lists (AKA multidimensional lists) are used frequently in programming to represent tables

# You can also print out the data in a table format
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()
    
# How to create a table that lists 1 - 5
#1 2 3 4 5
#1 2 3 4 5 
#1 2 3 4 5
#1 2 3 4 5


# We start with one line
table = [i for i in range(1, 6)]
print(table) 

# Then we print out multiple lines
table = [[i for i in range(1, 6)] for j in range(4)]
print(table) 





# Adding and Multiplying lists

# Adding lists
list_us = ['New York City', 'Chicago']
list_uk = ['London', 'Bristol']
list_all = list_us + list_uk
print(list_all)


# Multiplying Lists
list_numbers = [0, 1] * 10
print(list_numbers)







# Further string features

# We can use indexing and slicing with strings to read individual characters or groups of characters
fav_band = 'Green Day'
print(fav_band[6])

print(fav_band[:6])

# We can use methods to transform our string somehow and give us a new string
# An example would be a lower case string to upper case string

text = 'please capitlize me'
text_cap = text.upper()
print(text_cap)


#We also have string methods that return 'true' or 'false'
# We also have methods that can recognize when a number is in a string

user_number = input('Please provide a numeber: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')
    
