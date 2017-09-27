epsilon = 0.01
y = 24.0
guess = y/2.0
numguess = 0

while abs(guess*guess - y) >= epsilon:
    numguess += 1
    guess = guess - (((guess ** 2) - y)/(2 * guess))
print ('numguess = ', str(numguess))
print ('sqroot of ' + str(y) + 'is' + str(guess))




