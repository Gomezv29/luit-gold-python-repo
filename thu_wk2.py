# Introduction to writing functions

# Functions are separated fragments of code that do one well defined thing
# Writing your own functions can divide your code into well, isolated pieces, especially with longer programs

# Whats great about writing functions is that you can define it once and use it over and over in your code
# That way if something is wrong you can check the function first and will only have to fix it the once instead of going through all of the lines in your code

# An example function is
def greet ():
    print('Hello, my dear!')


print(greet())



# Functions with parameters

# Parameters are various values that we pass to a function
# ex: we need to find the average from multiple #'s in a list

input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

sum = 0.0
for number in input_numbers:
    sum += number
average = sum / len(input_numbers)

print(average)

# We want to turn the above code into a function. How we do that is below:
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)

    print(average)
    
    
# A Parameter is a special kind of variable and can only be defined inside the pair of [] after the function name and ONLY exists in the given function

# We can call the function:
get_average([5.0, 3.5, 7.8, 9.9, 10.0]) # The list inside the [] is called an argument


# When you invoke a function you must provide all of its arguments

# You must also make sure that you are passing the correct type of value
# In the above example we're expecting a collection such as a list or a tuple with numbers inside. If you use something else you'll get an error



# You can also define functions with more than one parameter

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
# Now when you invoke a function somewhere in your code, you'll need to provide both of them
print_letter_count('Welcome', 'e')

# A more complicated example
print_letter_count('People say nothing is impossible, but I do nothing every day.', 'a')

# The order of arguments is important for example
print_letter_count('e', 'Welcome')

# Below we use the parameter name with the = operator to specify which value should go to which parameter
print_letter_count(text='Welcome', letter='e')

#Now that we use named arguments, we can swap the places and the function call will still be correct
print_letter_count(letter='e', text='Welcome')







# Default Parameter values
            # In an earlier note the sep and end parameters of the print function were introduced like so
print('Hello', 'How are you?', end='.', sep='-')
            # End and Sep are keyword arguments or named arguments
            # Which are arguments which you use at the end of a function invocation AFTER all the positional arguments
            # They are ALWAYS optional and ALWAYS have a default value


#Let's see how keyword arguments work with your own created functions
def print_letter_count(text, letter='a'):  # for when we'll mostly be counting the letter A in a string
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
    
# Now we can invoke the function with only 1 value
print_letter_count('How many letters a are here?')


# We can invoke a function with NO arguments because BOTH parameters have default values below:
def print_letter_count(text='This is the default string to search', letter='a'):  
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

print_letter_count()

# When defining a vale and its parameters, you can mix parameters with and without default values


##### REMEMBER ##### all positional arguments must appear before any named arguments





# Name scopes

# In this course, when they say the scope of a name, we will refer to a variable name

# The scope of a name is the part of the code where the name is properly recognizable and can be used

# We can also define mysterious var inside the function definition

def show_truth():
    mysterious_var = 'Surprise!'
    print(mysterious_var)
show_truth()


# Below is an example of Shadowing
def show_truth():
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
    
mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)
# If there was NO shadowing, then functions written by other people could accidentally change the values of our global variables and we wouldn't know whats happening

def show_truth():
    global mysterious_var            # This instruction means: don't use shadowing for the variable named mysterious var
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
    
mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)

# Definitely KNOW the global command for the exam, but its not usually used in real world applications


# There is something we have to be aware when working with lists
def show_truth():
    mysterious_var = ['New Surprise!']
    print(mysterious_var)
    
mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)




def show_truth():
    mysterious_var.append('New Surprise!')
    print(mysterious_var)
    
mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)







# The None value

# Functions can typically
# 1. Cause some effect
# 2. Return a meaningful value

# One function can do both of those things at the same time

# The print function is a great example of a function that doesn't return any meaningful value, it only causes some effect
print('hello')

# Len on the other hand is a function that doesn't cause any effect, but it returns a meaningful value
len('hello')
        # We can then assign this return value to a variable and use it in a loop
length = len('hello')

# Input is a function that does both things at the same time
    # It causes an effect by prompting the user to provide a value and it also returns the value to us
number = input('what is the number?')

# experiment
print_return = print('Hello world')
print(print_return) # shows us 'Hello world' and 'None'

# None is used to describe a null value or no value at all
# None is a special value
# None is NOT zero
# None is NOT false
# None is NOT the same as an empty string
# ONLY none can be none

x = None

if x:
    print("None is True")
elif x is False:
    print("None is False")
else:
    print("None is not True, or False, None is just None")
    
# None is neither true or false
x = None
if x is None:
    print('yes')
if x == None:
    print('it does')
    
# None is a value returned implicitly by functions that don't return anything meaningful

def greet():
    print('hello!')

x = greet()
print(x)





# The Return keyword

# Return keyword is used to return a meaningful value
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average   # We DO NOT use brackets around return because it is NOT a function
    
print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

# We can also save the return value in a variable and then later use it in our code somehow
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')
    
# The keyword return actually does 2 things at the same time
     # It gives the result, but it also immediately exits the function
     # This means that any instruction after the return statement will be ignored

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me!') # function execution was terminated before it could reach this instruction
    
print(get_average([2]))

# This feature is sometimes used when we want to exit a function without returning anything meaningful
     # All we have to do is use the keyword return alone without any expression or value

def is_first_last_equal(number_list):
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False

print(is_first_last_equal([10, 20, 30, 40, 10]))  # This will give us true

print(is_first_last_equal([10, 20, 30, 40, 50]))  # This will give us false


def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
        
print(is_first_last_equal([])) 