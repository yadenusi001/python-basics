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