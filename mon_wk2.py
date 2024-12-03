# Intro to lists

number = 2
number = 5 # will make the first 'number =' obsolete


# There are 3 types of collections
# 
# lists
# tuples
# dictionaries


# Lists are usually used to store values of the same type

city_1 = 'New York City'
city_2 = 'Los Angeles'
city_3 = 'Chicago'
city_4 = 'Houston'
city_5 = 'Phoenix'

# An easier way to show the above would be in a list, like below

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']  # Lists will always use [], and the items inside are numbered. So New York City = 0
print(top_cities)

# REMEMBER List indices start at 0.

# to get a particular item in the list you'll have to use the []. This is called Indexing
print(top_cities[1]) #ex of Indexing
print(top_cities[0])
print(top_cities[4])

# You can also use negative numbers in Indexing. It will just read the list from the right-hand side.
print(top_cities[-1])  # This gives us the city Phoenix which is the same as top_cities[4]


# To access a few, but not all the elements at the same time we use 'Slicing'
# To get the first 2 elements you can use below
print(top_cities[0:2]) 

print(top_cities[2:]) # This means start at the 2nd element and continue the list
print(top_cities[:3]) # This means start the list and stop at element 3







# Deleting List elements

top_cities_2 =['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
# We only want US cities in our list. To delete an element from the list we'll be using 'del'
del top_cities_2[2]
print(top_cities_2)
print(top_cities_2[2]) # This prints out 'Chicago' because the elements will shift to the left to fill in the hole of the deleted element
del top_cities_2[3:] # This instruction is to delete all elements AFTER element 3
print(top_cities_2)
del top_cities_2[:] # This will delete the whole list
print(top_cities_2)

# You can also delete the entire list by typing in 'del list_name' and when you try and print the list you'll just receive an error'






# Adding New Elements to the List

book_ratings = [7, 9, 5, 6, 8]

book_ratings.append(4) # append is a method. A Method is invoked using its name and a pair of brackets with arguments inside
# Unlike normal f()'s, methods are invoked with a dot after the data they work on.
# If you were to try append by itself you would just get an error

# You need the list in order for .append to work

# REMEMBER methods are functions that "belong" to specific data.


# Another way to insert data into a list is with the ".insert" method
book_ratings.insert(1, 10)
print(book_ratings)








# Iterating Lists

for city in top_cities:
    print('Current city:', city)
# The loop will print out the list in order

# You can also use a different way to show the element and its index
for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:', top_cities[city_index],)  # The len function we used with strings and it returns the # of charactes.
# With Lists, len returns the number of elements


# For the next ex. We need to sum up all the #'s in the list and print the total amount of money
spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent:', sum)  # This is a simple way of adding up all the #'s in a list