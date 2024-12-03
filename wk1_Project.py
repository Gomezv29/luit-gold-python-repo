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

#dept = input('What department will the EC2\'s be under? ')
#ec2 = int(input('How many EC2 instances would you like names for? '))

#i = 1
#N = 8

#res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))

#while True:
 #   print(dept + str(res), i)
  #  i += 1
   # if i > ec2:
    #    break
#print('Here are your EC2 names!')




# Attempt 14

#dept = input('What department will the EC2\'s be under? ')
#ec2 = int(input('How many EC2 instances would you like names for? '))

#i = 1
#N = 8
#L = [string.ascii_letters, string.digits]

##res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
#random.shuffle(L)
#shuf = ''.join(L)

#while True:
 #   print(dept + shuf, i)
  #  i += 1
   # if i > ec2:
    #    break
#print('Here are your EC2 names!')




# Attempt 15

#dept = input('What department will the EC2\'s be under? ')
#ec2 = int(input('How many EC2 instances would you like names for? '))

#i = 1
#N = 8
#L = [res]

#res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
#random.shuffle(L)
#shuf = ''.join(L)

#while True:
 #   print(dept + shuf, i)
  #  i += 1
   # if i > ec2:
    #    break
#print('Here are your EC2 names!')







# Attempt 16

#dept = input('What department will the EC2\'s be under? ')
#ec2 = int(input('How many EC2 instances would you like names for? '))
##res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))

#i = 1
#N = 8
#L = [random.choices(string.ascii_letters, string.digits)]

#random.sample(L)
#shuf = ''.join(L)

#while True:
 #   print(dept + shuf, i)
  #  i += 1
   # if i > ec2:
    #    break
#print('Here are your EC2 names!')




# Attempt 17

#dept = input('What department will the EC2\'s be under? ')
#ec2 = int(input('How many EC2 instances would you like names for? '))

#i = 1
##L = [random.choices(string.ascii_letters, string.digits)]
#res = ''.join(random.sample(string.ascii_letters + string.digits for ec2 in range(8))
##random.sample(L)
##shuf = ''.join(L)

#while True:
 #print(dept + res, i)
 #i += 1
 #if i > ec2:
  #break
#print('Here are your EC2 names!')




# Attempt 18

#dept = input('What department will the EC2\'s be under? ')
#ec2 = int(input('How many EC2 instances would you like names for? '))

#def get_random_name():
 #name_source = string.ascii_letters + string.digits
 #for ec2 in range(8):
  #name += random.choice(source)
  #name_list = list(name)
  #random.SystemRandom().shuffle(name_list)
  #name = ''.join(name_list)
  #return name
  
#i = 1

#while True:
 #print(dept + get_random_name(), i)
 #i += 1
 #if i > ec2:
  #break
#print('Here are your EC2 names!')





# Attempt 19  **Success for Part 1*

#dept = input('What department will the EC2\'s be under? ')
#ec2 = int(input('How many EC2 instances would you like names for? '))

#def get_random_name():
 #name_source = string.ascii_letters + string.digits
 ## select  lowercase
 #name = random.choice(string.ascii_lowercase)
 ## select  uppercase
 #name += random.choice(string.ascii_uppercase)
 ## select  digits
 #name += random.choice(string.digits)
 
 #for n in range(8):
  #name += random.choice(name_source)

 #name_list = list(name)
    ## shuffle all characters
 #random.SystemRandom().shuffle(name_list)
 #name = ''.join(name_list)
 #return name
  
#i = 1

#while True:
 #print(dept + get_random_name())
 #i += 1
 #if i > ec2:
  #break
#print('Here are your EC2 names!')





# Attempt 20 + Advanced

dept = input('What department will the EC2\'s be under? ')
ec2 = int(input('How many EC2 instances would you like names for? '))

def get_random_name():
 name_source = string.ascii_letters + string.digits
 # select  lowercase
 name = random.choice(string.ascii_lowercase)
 # select  uppercase
 name += random.choice(string.ascii_uppercase)
 # select  digits
 name += random.choice(string.digits)
 
 for n in range(8):
  name += random.choice(name_source)

 name_list = list(name)
    # shuffle all characters
 random.SystemRandom().shuffle(name_list)
 name = ''.join(name_list)
 return name
  
i = 1

while True:
 if dept == 'Marketing' or dept == 'marketing' or dept == 'Accounting' or dept == 'accounting' or dept == 'FinOps' or dept == 'finops':
  print(dept + '_' + get_random_name())
  i += 1
  if i > ec2:
   break
 else:
  print('Sorry, you are not authorized to use this Name Generator')
  break 
print('Here are your EC2 names!')