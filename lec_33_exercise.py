
print('''
============================
=== PYTHON GUESSING GAME ===
============================
''')

year_released = 1994

user_input = int(input('When was Python 1.0 released? '))
while user_input != year_released:
    if user_input < year_released:
        print('It was later than that!')
        user_input = int(input('When was Python 1.0 released? '))
    if user_input > year_released:
        print('It was earlier than that!')
        user_input = int(input('When was Python 1.0 released? '))
print('Correct!')



# Exercise Solution
#while True:
   # answer = int(input('When was Python 1.0 released? '))
    #if answer > 1994:
       # print('It was earlier than that!')
   # elif answer < 1994:
        #print('It was later than that!')
    #else:
        #print('Correct!')
        #break