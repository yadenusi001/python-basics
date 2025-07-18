our_number = 42

# get input from the user

guess = int(input("Enter your guess"))

# conditional statement to check the guess

if guess == our_number:
    print ('Hooray!')
elif guess > our_number:
     print ('Too high!')
else:
     print('Too low!')



counter = 1 
while counter < 20: 
    if counter % 3 == 0 and counter % 5 == 0: 
        print (f'{counter}: Fizzbuzz') 
    elif counter % 3 == 0: 
        print(f'{counter}: Fizz') 
    elif counter % 5 == 0: 
        print(f'{counter}: Buzz') 
        + 1 
        counter+= 1 # This is a shortcut for counter = counter 
else: 

    print ('Done with while loop')