# Intro to Tuples
# Tuples are similar to lists in that its a type of collection
# Tuples are created with round brackets
empty_tuple = ()
one_el_tuple_a = (1,) # we added a comma due to syntax reasons. The comma tells Python that we're trying to create a tuple and not a single value
one_el_tuple_b = 1,

three_el_tuple = 1, 2, 3  # When you have multiple elements in your tuple the LAST comma is optional
print(three_el_tuple) # The print function will always show your tuples in the same way even when you omit the last comma and brackets



# The biggest difference between lists and tuples are 'Mutability'

# There are 2 types of data in Python.
# mutable data
# Immutable data

# Mutable data can be freely updated whenever you want. Lists are a good example
# 
# Immutable data is data that cannot be updated. Tuples are a good example. When you first create a tuple, it stays that way forever. 


# You can use the assignment operator again to assign a new tuuple to the user data variable
user_data = ('John', 'American', 1964)
user_data = ('Katya', 'Russian', 1980)

# Methods will NOT work on tuples. You will get an error if you try to use the .append method on a tuple
# you CANNOT delete elements using del in tuples either


# You CAN use indexing and slicing with tuples, but NOT to change individual elements
print(user_data[0])
# user_data[0] = 'Mark'  is not allowd




# Strings in Python are also immutable
message = 'welcome'
message = 'Welcome' # This is fine

# message[0] = 'W' is not allowed and will give you an error





# Tuple Operations

# Theres the Len function to count the number of elements in a tuple
user_data = ('John', 'American', 1964)
print(len(user_data))

# You can use the in and not in operators the same way as with lists
user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US!')
    
# You can also use for loops with tuples too
user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)
    
    
    
# Tuples can also be added together or multiplied by an interger
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data) 
# when we added tuples together they will create a new tuple, since we can't make changes to tuples

# For multiplying tuples
numbers = (0, 1) * 10 # This makes a sequence of repeating 0, 1 's
print(numbers)

# Lists are typically used in situations when you want to have many values of the same data type
male_name = ['Adam', 'Jerry', 'Mark'] # list example
# Even though each element is a different name, they are all strings and they all represent male names

# Another ex. could be line tempertures
berlin_temps = [13.0, 17.5, 12.0] # all elements are floats and temperatures


# Tuples on the other hand, are used when you want to group together values of different types that are somehow related
user_data = ('John', 'American', 1964) # here we have 3 elements that are different data types. We have 2 strings and an interger
# All 3 elements are related because they describe one user 'John'

# Tuples are also used to perform certain Python operations quicker. We can see this in a previous example
first = 5
second = 7
first, second = second, first # both statements on either side of the = are tuples



# Tuples in lists, lists in tuples

# Python allows you to put lists as tuple elements and vice versa

# Example of Tuples in lists
city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)]

for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])
    
    
# Lists in tuples
user_data = ('John', 'American', 1964) # We'll add 'John's weight' to keep track
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5]) # what's interesting is that you can't add another list or any other elements to the tuple
# but you can add more weight measurements to the list inside the tuple
user_data[3].append(79.6)
print(user_data)