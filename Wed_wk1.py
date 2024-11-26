# Type casting is changing one fucntion to another. ex: changing an interger into a float or a float into a string.
# you cannot divide and interger with a float, so we use the float() to change the interger into a float. There are 2 ways this can be accomplished.
height_cm = input('Height converter: enter your height in cm: ')
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48 )

weight_pd = float(input('Weight converter: enter your weight in pounds: '))
print('Your weight in grams is:', weight_pd * 453.592 )

# Likewise if you need an interger you can use the int() 
year_born = int(input('What year were you born? '))
print('In 2100, you will be', 2100 - year_born, 'years old, provided you live this long')

# You can also convert an interger and float into a string using str()
temp_c = input('Enter the temperature today in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + ' degrees Fahrenheit'
print(temp_statement)



# More about operators
# the + and - signs we call Binary Operators
# There are also Unary Operators which is using the + or - infront of a number
print(+12) #example of a Unary operator
print(-2)

# Order of Operators
# 1. **
# 2. * / // %
# 3. + -
print(2 + 3 * 2)
print((2 + 3) * 2)

# Python will round your float numbers
print(0.1 + 0.1 + 0.1)
# REMEMBER: The precision of floats is limited

# Tricky operations
# In the below Python will start from the right
print(2 ** 2 ** 3)
# REMEMBER: The exponentation operator (**) uses right-sided binding (i.e. starts from the right)


# More about print() and strings
# len() will accept a string and return the number of characters in the string
print(len('Hello!'))

# New function: Keyword arguments/named arguments that you can use at the end of an argument or evocation
# introduced by using the argument name and an = , and are always optional
print('Hello, World!', end='.')
print('Python speaking!')
# another keyword is the 'sep' argument specifies the seperator between the values printed to the output
first_name = 'Jane'
print('Your first name is', first_name, 'Welcome!', sep='-', end='=')


# Bit Operators
# There are 6 bitwise operators that you can use to minipulate data
# & means and
# | means or
# ~ is a logical negation (logical NOT)
# ^ means exclusive or (xor)
# << works by multiplying by a certain power
# >> works by dividing by a certain power

# The first four
first_bit = 1
second_bit = 0

print(first_bit & second_bit) # Will equal 0. You will only see 1 when both bits are 1.
print(first_bit | second_bit) # Will equal 1 when at least one of the bits is 1. Otherwise it will be 0 when both bits are 0
print(first_bit ^ second_bit) # Will equal 1 when one bit is 1 and will equal 0 when both bits are 0
print(~1) # Will equal -2
print(~0) # Will equal -1 

# the shift operators ( << and >>) are typically used on longer bit sequences
print(12 << 1) # This will equal 24 or twice as much
print(12 << 2) # This will equal 48 or 4 times as much
print(12 >> 1) # This equals 6 or divided by 2
print(12 >> 2) # This equals 3 or divided by 4