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
