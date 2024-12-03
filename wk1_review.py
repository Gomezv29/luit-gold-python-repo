import random

# Generate a random interger between 0 and 10
number = random.randint(0, 10)

# Check if the number is less than 6
#if number < 6:
 #   print('small number') # If true, print "small number"
# If the number is greater than 6
#elif number > 6:
 #   print('big number') # If true, print "big number"
# If neither of the above conditions is met, meaning the number is equal to 6
#else:
 #   print('number is 6') # If true, print "number is 6"


# Check if the number is less than 4
#if number < 4:
 #   print('really small number') # If true, print "really small number"

# Print the enerated number
#print(number)




# Initialize a counter for the number of iterations
counter = 0

# Use a while loop to repeat the following block of code until the condition number != 7 is met
while number != 7:
    # Check if the counter has reached 13
    if counter >= 13:
        # If it has, exit the loop
        break
    
    # Generate a new random number between 0 and 10
    number = random.randint(0, 10)
    # Increment the counter by 1
    counter += 1 # counter = counter + 1

# Print the number of iterations and the final number
print(counter, number)


# Use a for loop to iterate over a range of values from 0 to 4
for i in range(5):
    # Print the square of each value
    print(i**2)