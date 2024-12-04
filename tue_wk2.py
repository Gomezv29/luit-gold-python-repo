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