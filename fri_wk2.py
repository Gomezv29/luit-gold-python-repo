# Introduction to exceptions

# One of the most popular errors is the syntax error. Ex: forgetting to indent
if True:
print('hooray!')

value = int(input('Enter an integer: '))
print('The inverse of', value, 'is', 1/value)
# The above will give you a value error if you input a letter instead of an interager


# An exception is an event which occurs during the execution of a program that disrupts the normal flow of the program's instructions

# When Python gets something it didn't expect it won't know what to do and thus raises an exception

try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except:
    print('You did not provide a number, so I will not calculate the inverse') # This is the part of the code that handles the exception
    
# When we input 0 above we don't want either of the prints to happen

# First, we'll need to note down all the specific names of the exceptions thrown when the user provides something that is not a number and not 0

try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
    
# The number of accepted branches is not limited, bu none of the exceptions can be specified more than once.


try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
except:
    print('Something strange happened here, sorry') # If any other exception is raised then this last default block will be used
    
    

# Can you catch SyntaxErrors?
# I've mentioned that you can use the default except block to catch any sort of exception:

try:
  # your code
except:
  # any exception

#However, there is one special exception type: SyntaxError. You should pay attention to how it works.

#If you raise a SyntaxError manually, then you can catch it in the except block just fine:

try:
  raise SyntaxError
except:
  print('Got it!') # SyntaxError is caught here

#However, if you make a syntax error in the try block and Python automatically raises a SyntaxError for you, then you cannot catch it:

try:
  5:4 # this line generates a SyntaxError
except:
  print('Got it!') # SyntaxError is NOT caught here
  
  
  

# Exception hierarchy

# Python has over 60 built in exception types

# at the top is: BaseException
#                      Exception,   SystemExit,    KeyboardInterrupt
#                           ArithmeticError,   LookupError,   TypeError,   ValueError
#                               ZeroDivision Error,      IndexError
#                                                        KeyError




# SystemExit is a method used to terminate, or aka closure program
import sys  # We import this in order to use sys.exit()

user_name = input('What is your name? ')
if user_name == ' ':          # Checking to see if user input provides an empty name
    print('Empty name? I cannot work with that. I am closing the program. Bye!')
    sys.exit()
print('Hello,', user_name)
print('Let us get started...')


# KeyboardInterrupt is raised when the user presses a key combination that causes an interrupt to the executing script
#while True:
 #   print('hi!')   For Jupyter you'd press the interrupt the colonel
 
 

# Exception is similar to BaseException
    # The difference is BaseException is typically only used as a template for inter Python exceptions
    # While Exception can also be used as a template for your own exceptions
# Also a template for other exceptions


# ArithmeticError is the base class for a variety of mathematical arithmetic errors
     # ZeroDivisionError is underneath 
     

# LookupError has two 'children' underneath: IndexError and KeyError
    # Those 2 exceptions will appear when you work with collections such as lists or dictionaries
programming_languages = ["Java", "Python", "C++"]
print(programming_languages[10])
# We get an IndexError because we ask for index of 10 which is not in the list

#Ex of KeyError - Happens when you work with dictionaries
ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
print(ages['Michael'])
# We get a KeyError because 'Michael' is not present in the dictionary


# TypeError indicates that the type of data you're trying to use is not correct in the given context
age = input('What is your age? ')
print('In 10 years, you will be', age + 10) 
# When you provide an age of 25 it will show you the error because it can only concatenate string to string NOT intergers


# ValueError is raised when a function or method 2 receives an argument of the correct type, but with an actual value that is invalid for some reason
age = int(input('What is your age? '))
print('In 10 years, you will be', age + 10) 
# When you provide something that is NOT an interger like 'a', you can see the valueerror l



# The difference between TypeError and ValueError is that we use the incorrect variable types.
    # and with ValueError the type of variable is correct but the content of the string is not correct
    
    
    
    
# Propagating Exceptions
# Program below asks for certain information about a user's birthday

def get_day(user_info):
    day = int(input('What is the day of your bday? '))
    user_info.append(day)
    
def get_month(user_info):
    month = int(input('What is the month (1-12) of your bday? '))
    user_info.append(month)

def get_year(user_info):
    year = int(input('What is the year of your bday? '))
    user_info.append(year)
    
def get_user_bday(user_info):  # This function calls 3 other functions
    get_day(user_info)
    get_month(user_info)
    get_year(user_info)
    print('So your bday is', user_info)
    
print('Hi, I will collect some info about your bday!')
user_info = []
get_user_bday(user_info)

# Because the functions require an integer we can run into ValueError problems


def get_day(user_info):
    day = int(input('What is the day of your bday? '))
    user_info.append(day)
    
def get_month(user_info):
    month = int(input('What is the month (1-12) of your bday? '))
    user_info.append(month)

def get_year(user_info):
    year = int(input('What is the year of your bday? '))
    user_info.append(year)
    
def get_user_bday(user_info):  # This function calls 3 other functions
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print('So your bday is', user_info)
    except ValueError:
        print('You entered incorrect data, bye!')
    
print('Hi, I will collect some info about your bday!')
user_info = []
get_user_bday(user_info)


# In Python, exceptions are Propagated through functions




# Assertion exceptions

#There are 2 ways to do that but PCP exam will only require you know one

# Assertions are assumptions in our program that should always be true

def calculate_inverse(number):
    assert (number != 0), 'Got 0 as a number!'
    return 1/number
print(calculate_inverse(0))
# We'll get an AssertionError
      # Which is ALWAYS called when we use the keyword assert and the condition privileges within the brackets is NOT satisfied 
      
# In General, Assertions are used for debugging and testing of code

# You can add assertions as sanity checks at the beginning of a function to make sure that it recieves correct data

# Also Assertions are sometimes used to document your code

# DO NOT
     # Validate user input with assertions
     # Handle AssertionErrors in try... except