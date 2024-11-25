#variable examples
greeting = 'Hello, friend!'
print(greeting)
greeting = 'Hi, everbody!'
print(greeting)




#Intergers
age = 35

#Below has examples of Floats
speed1 = 4.5
speed2 = 4.0
speed3 = 4.

#Back to interger
speed4 = 4

#Boolean values
am_i_ugly = False
#am_i_ugly2 = true
#Boolean True or False values MUST start with a Capital letter or else you'll receive an error'
#Remember by convention 1 = True and 0 = False




#Comment Examples
print('sample') # here is a mid-line comment
# here is an all-line comment
#Comments help us document our code if it is going to be read by others
#Comments are also helpful to quickly de-activate part of the code
print('Hello')
#print('Hidden message')



#Numerical representations examples
# underscores in numbers
12000300
12_000_300

#scientific notation
# 3e4 = 3E4 = 3 * 10000 = 30000
# 3e-4 = 3E-4 = 3 * 1/10000 = 0.0003
print(0.000000000000000000000000003)

# octal numbers not commonly used but will be on exam
# start with 0O or 0o is an octal number
print(0o123)

# hexadecimal numbers
# start with 0X or 0x
print(0x123)



# Operators
# Addition
2 + 3

# Subtraction
5 - 4

#Multiplication
3 * 5

# Standard Division
6 / 2
7 / 2

# Interger Division
6 // 2
7 // 2

# Modulus Divison. Returns the remander of the division
6 % 2
7 % 2

# Zero Division Error
#5 / 0

# Power operator
2 ** 3 # This is the same as 2^3



# Reassigning values
age = 28
print(age)
new_age = age + 5
print(new_age)
age = age + 7
print(age)
age += 7
print(age)
#Can also use age *= 2
# age -= 5
# age /= 3

# String concatenation = joining strings using +
text = 'hokus' + 'pokus'
print(text)
print('hokus' * 5)
print(23+5) # vs
print('23' + "5")


# Input() function
print('What is your name?')
user_name = input ()
print('Hello,', user_name)
# Functions in Python can:
# 1. Cause some effectS
# 2. Return a value
# Another way of writing it is
user_age = input('What is your age?')
print('Oh really?', user_age)