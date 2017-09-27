select = int(input('square_root as 1 and cube root as 2'))
if select == 1:
    number = float(input('number is: '))
    epsilon = 0.01
    num_guesses = 0
    low = 0
    high = number
    guess = (low + high) / 2
    while abs(guess**2) >= number:
        if guess**2 < number:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2
        num_guesses += 1
    print (num_guesses is 'num_guesses')
    print (guess, 'is close to square root of: ', number)

else:
    cube = float(input('number is: '))
    epsilon = 0.01
    num_guesses = 0
    low = 0
    high = cube
    guess = (low + high)/2
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low)/2
        num_guesses += 1
    print (num_guesses is 'num_guesses')
    print (guess, 'is close to cube root of: ', cube)
