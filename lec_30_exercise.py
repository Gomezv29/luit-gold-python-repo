day_purchased = int(input('How many days ago have you purchased the item? '))
usage_when = input('Have you used the item at all [y/n]? ')
item_broken = input('Has the item broken down on its own [y/n]? ')

if item_broken == 'y' or day_purchased <= 10 and usage_when == 'n':
    print('You can get a refund.')
else:
    print('You cannot get a refund.')
    
    
    
    
    
    # Solution
purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.')