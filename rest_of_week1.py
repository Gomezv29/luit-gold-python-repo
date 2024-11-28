# If statements
user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old') # Recommendation is to use 4 spaces for the indentation
    print('Sorry, you do not qualify')
# We can have multiple elif statement
elif user_age == 30:  # We use 2 '=' to equal exactly 30 because 1 '=' assigns a value
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are 30 years old or younger')
    print('Congratulations, you qualify!')
    
    
    
    # Logical operators and Conditions
    
    # <   less than
    # >   greater than
    # <=  less than or equal 
    # >=  greater than or equal
    # ==  equals
    # !=  not equals
password = input('Do you know the secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct password')
    
if 2 == 2:
    print('true')
if 1 ==2:
    print('true')
if 2 == 2.0:
    print('true')
    
    
    
# Joining multiple conditions
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a Gerrman student exchange programme')
else:
    print('Sorry, you do not qualify')
    
user_country = input('What is your country? ')
if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange programme')
else:
    print('Sorry you do not qualify')
    
    
user_country = input('Where do you com from?')
if not user_country == 'Germany':
    print('You are not from Germany!')
else:
    print('You are from Germany')


user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germany' and user_age < 25 or \
    user_country == 'Germany' and user_age < 23:   # for really long lines you can add a \ to continue the instruction on a different line
    print('You qualify!')
else:
    print('You don\'t qualify')
    
    
# Boolean operaters have their priorities

# !. not
# 2. and 
# 3. or

#Must know order above for exam 
# Recommended to use brackets in code to improve readability. Brackets will NOT change the order above.

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if ((not user_country == 'Germany') and user_age < 25) or \
    (user_country == 'Germany' and user_age < 23):   # for really long lines you can add a \ to continue the instruction on a different line
    print('You qualify!')
else:
    print('You don\'t qualify')
    
    
    
# Nested if statements
answer_a = input('Do you like travelling? y/n: ')
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n: ')
# Proper indentation is very important for nesting
    if answer_b == 'y':
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry to hear that!')
else:
    print('Sorry to hear that!')