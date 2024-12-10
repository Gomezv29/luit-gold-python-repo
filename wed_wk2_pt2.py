# Introduction to dictionaries

# Dictionaries are collections used to store key value pairs
# Dictionaries are Mutable

emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'peters@yandex.com',
    'Mark Steel': 'mark@steel.com'
}

# To find an email in a dictionary
print(emails['Mark Steel'])


# Another example

spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pajaro'
}

print(spanish_animals['cat'])

# Dictionaries are typed with {} curly braces and then you add the key value pairs inside

# the format is key value : key value ; and each key must be unique
# If you have 2 of the same key pairs, Python will use the latest one

# Keys can be any immutable data type. You can have strings, intergers, floats, and tuples in dictionaries but NOT lists

tennis_ranking = {
    1: 'Ashleigh Barty',
    2: 'Naomi Osaka',
    3: 'Simona Halep'
}



# Below will give you an error because Lists CANNOT be used as key values in dictionaries
#tennis_ranking = {
 #   1: 'Ashleigh Barty',
  #  2: 'Naomi Osaka',
   # 3: 'Simona Halep'
#}



# While a list CANNOT become a key it CAN become a value
city_ratings = {
    'Bangkok': [7, 4, 7, 5],
    'Hanoi': [7, 6, 4, 5],
    'Manila': [6, 6, 4, 4, 5]
}






# Dictionary Operations

# we can create an empty dictionary by just adding curly braces
grades = {}

# We can add entries to the dictionary like below
grades['Jane'] = 'A-'
grades['Anne'] = 'B'

print(grades)

# If we want to update an entrie in the dictionary we can do so
grades['Anne'] = 'A'

# We can also use the update method to update an entry
grades.update({'Jane':'A'})

print(grades)


# We can also check the # of key value pairs in a dictionary using the Len function
print(len(grades))


# We can cheeck if a given key is present with a familar operator
if 'Jane' in grades:
    print('Jane got:', grades['Jane'])
    

# to delete a given key alongside its value you CAN use the del operator
del grades ['Jane']
print(grades)


# prior to Python 3.6 dictionaries were not ordered

# We can still iterate a dictionary and one way is below
grades = {}
grades['Jane'] = 'A-'
grades['Anne'] = 'B'

# We can use a simple 'for' loop the same way as for lists to get access to the keys
for el in grades:
    print(el)

# We'll get the same as the immediate above example by using the keys method on the dictionary
for el in grades.keys():
    print(el)

# If you want to get access to the values instead, and the values alone, you can use the method named values for L in greates values
for el in grades.values():
    print(el) # This will only show you the values ('A-', 'B')
    
    
# If you want to get access to both the keys and the values you can use method named items
for person, grade in grades.items():
    print(person, 'got', grade)
