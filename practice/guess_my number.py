low = 0
high = 100
guess = abs((low+high)/2)
print ('Please think of a number between 0 and 100!')
print('Is your secret number', guess, '?')
while True:
    my_guess = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low."
                         " Enter 'c' to indicate I guessed correctly. ")
    if my_guess == 'h':
        low = guess
        guess = abs((low + high)/2)
        print('Is your secret number', guess, '?')
    elif my_guess == 'l':
        high = guess
        guess = abs((low + high)/2)
        print('Is your secret number', guess, '?')
    elif my_guess == 'c':
        print ('Game over. Your secret number was: ', guess)
        break
    else:
        print ("enter valid input")
