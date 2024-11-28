day = int(input('How many days ago have you purchased the item? '))
usage = input('Have you used the item at all y/n? ')
item = input('Has the item broken down on its own y/n? ')

if day < 10 and usage == 'y' and item == 'n' and item == 'y' or day > 10 and usage == 'n' and usage == 'y' and item == 'y':
    print('You can get a refund')
else:
    print('You cannot get a refund')