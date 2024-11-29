# The While loop
#while condition:
 #   do_somthing()
  #  do_somthing2()

counter = 1
while counter < 11:
    print(counter)
    counter += 1 # do not forget to increment the variable in the while loop or else the value will always be 1 and just keep printing out 1
print('Finished!')

# Remember an infinite loop never ends (its condition is always true)
# Remember Increasing by 1 is called incrementation.
# while loops are used when we don't know how many times the main body should be executed.


# If you use ''' in the beginning and end of the print() then python will print out multi-line strings exactly how you type it out
secret_number = 14
print('''
==========================
=== SECRET NUMBER GAME ===
==========================
''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
 print('Wrong!')
 user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You hve guessed the secret number.')





# The for loop
# Typically used to go through all the sequences
for letter in 'hello!':
  print('Current letter:', letter)
  
  
for counter in range(1,11):
 print(counter)
print('Finished!')

# You can input 1 # in the range and the counter will include 0
for counter in range(11):
 print(counter)
print('Finished!')


# You can even put 3 #'s in the range and the last number will be the increment'
for counter in range(1,11, 2):
 print(counter)
print('Finished!')

for counter in range(1,11, 4):
 print(counter)
print('Finished!')



# Break and continue
# break instructions are used inside loops. When Python reads a break it will exit the loop and move on to the next set of instructions outside of the loops
while True:
 name = input('Enter your name or EXIT to close the program: ')
 if (name == 'EXIT'):
  break 
 print('Hello', name)
 
 
 # If you want a counter but want to skip certain a certain #
 for i in range(1, 21):
  if i % 5 == 0:
   continue
  print(i)
 
 
# Other loop features
for i in range(11):
 pass

# Just like nested if statements you can use Nested Loops
for a in range(1,6):
 for b in range(1,6):
  print(a, 'x', b, '=', a * b)
  
  
  # Remember the else branch of a loop is ALWAYS executed exactly once (exception: break statement)
  i = 2
  while i < 5:
   print(i)
   i += 1
  else:
   print('else:', i)