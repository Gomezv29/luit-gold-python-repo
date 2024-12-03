print('''
***********************************
**** EC2 RANDOM NAME GENERATOR ****
***********************************
''')

# ATTEMPT 1

import random

#ec2 = int(input('How many EC2 instances would you like names for? '))
#dept = input('What department will the EC2\'s be under? ')
#random_number = random.randint(0,100000)
#ran_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#random_shuffle = ran_letter


#while ec2 <= 20:
 #   print('Here are your names: ', dept + random_shuffle + random_number)
  #  ec2 += 1
#print('Finished')


# Attempt 2

#ec2 = int(input('How many EC2 instances would you like names for? '))
#dept = input('What department will the EC2\'s be under? ')
#random_number = random.randint(0,100000)
#ran_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#random_shuffle = ran_letter


#while ec2 <= 20:
 #   print(dept, random_shuffle, random_number)
  #  ec2 += 1
#print('Finished')


# Attempt 3

import string

#ec2 = int(input('How many EC2 instances would you like names for? '))
#dept = input('What department will the EC2\'s be under? ')
#random_number = random.randint(0,100000)
#ran_letter = random.choice(string.ascii_letters)


#while ec2 <= 20:
 #   print(dept, ran_letter, random_number)
  #  random_number += 1
#print('Finished')



# Attempt 4

#ec2 = int(input('How many EC2 instances would you like names for? '))
#dept = input('What department will the EC2\'s be under? ')

#N = 8

#res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))


#while ec2 <= 20:
 #   print(dept + str(res))
  #  res += 1
#print('Finished')




# Attempt 5

#ec2 = int(input('How many EC2 instances would you like names for? '))
#dept = input('What department will the EC2\'s be under? ')

#N = 8

#res = ''.join(random.choices(string.ascii_letters, k=N))
#num = random.randint(0,1000)
 
#while ec2 <= 20:
 #   print(dept, str(res), num)
  #  num += 1
#print('Finished')



# Attempt 6

#ec2 = int(input('How many EC2 instances would you like names for? '))
#dept = input('What department will the EC2\'s be under? ')

#N = 8

#res = ''.join(random.shuffle(string.ascii_letters + string.digits, k=N))
 
#while ec2 <= 20:
 #   print(dept + str(res))
  #  break
#print('Finished')





# Attempt 7

#ec2 = int(input('How many EC2 instances would you like names for? '))
#dept = input('What department will the EC2\'s be under? ')

#N = 8

#res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
#rand = list(res)
#shuffle = random.shuffle(rand)
#rand = rand[:8]
 
#while ec2 <= 20:
 #   print(dept + shuffle)
  #  break
#print('Finished')



# Attempt 8

#ec2 = int(input('How many EC2 instances would you like names for? '))
#dept = input('What department will the EC2\'s be under? ')

#N = 8

#res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
#i = 1


#while ec2 in range(1,20):
 #   print(dept + str(res) + i)
  #  i += 1
#print('Here are your EC2 names!')



# Attempt 9

#ec2 = int(input('How many EC2 instances would you like names for? '))
#dept = input('What department will the EC2\'s be under? ')

#N = 8

#res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))


#while ec2 <= 20:
 #   print(dept + str(res), ec2)
  #  ec2 += 1
#print('Here are your EC2 names!')




# Attempt 10

#dept = input('What department will the EC2\'s be under? ')
#ec2 = int(input('How many EC2 instances would you like names for? '))

#i = 0
#N = 8

#res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
#shuf = random.shuffle(res, k=len(N))

#while True:
 #   print(dept + str(res), i)
  #  i += 1
   # if ec2 += 1
    #    break
#print('Here are your EC2 names!')



# Attempt 11

#dept = input('What department will the EC2\'s be under? ')

#i = 0
#N = 8

#res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))

#while True:
 #   ec2 = int(input('How many EC2 instances would you like names for? '))
  #  print(dept + str(res), i)
   # i += 1
    #if i == ec2:
     #   break
#print('Here are your EC2 names!')




# Attempt 12

#dept = input('What department will the EC2\'s be under? ')

#i = 0
#N = 8

#res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))

#while True:
 #   ec2 = int(input('How many EC2 instances would you like names for? '))
  #  print(dept + str(res), i)
   # i += 1
    #if i >= ec2:
     #   break
#print('Here are your EC2 names!')





# Attempt 13

dept = input('What department will the EC2\'s be under? ')
ec2 = int(input('How many EC2 instances would you like names for? '))

i = 1
N = 8

res = ''.join(random.choices(string.ascii_letters + string.digits, k=N)

while True:
    print(dept + str(res), i)
    i += 1
    if i > ec2:
        break
print('Here are your EC2 names!')