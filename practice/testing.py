"""
a = "hello"
b = "world"
c = a + b
'low' in b
print ('a' in a)

###########################################
print "hello world"
###########################################

a = 0
for i in range(5, 11, 2):
    a += i
print (a)
############################################
print (5 + 7 + 9)
############################################

n = 2
if n < 5:
    print ("happy")
else:
    print ("hello world")

###   infinite loop
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

######   looping
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)

#####    num
num = 10
while num > 3:
    num -= 1
    print(num)


####  break

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')
######################################################
i = 0
end = 6
total = 0
while i <= end:
    total += i
    i += 1
print (total)
############################################################
#end = 6
total = 0
for i in range (0, 7):
    total += i
print (total)

############################################################

count = 0
for letter in 'Snow!':
    print('Letter # ')
    #+ str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

###############################################################
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))
##############################################################
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')
################################################################
x= int(input('Enteran integer: '))
ans= 0
while ans**3 < abs(x):
    ans= ans+ 1
if ans**3!= abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x< 0:
        ans= -ans
    print('Cuberoot of '+ str(x) + ' is ' + str(ans))

###################################################################
cube = 8
for guess in range(cube+1):
    if guess**3==cube:
        ##print ('cube root of'+cube +'is'+ guess)
        print ("cube root of", cube, "is", guess)

#############iterations
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
    ##################################################
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break
######################################################################
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
######################################################################
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
######################################################################
"""


"""def adjacentElementsProduct(inputArray):
    product = []
    for i in range(len(inputArray) - 1):
        product.append(inputArray[i] * inputArray[i+1])
    return max(product)
    #######################################
def shapeArea(n):
    if n == 1:
        return (1)
    if n >= 2:
        return ((4*(n-1)) + shapeArea(n - 1))


print (shapeArea(2))
print (shapeArea(3))
print (shapeArea(4))

"""
def test(x):
    print x
    if x % 3 == 0 : return test(x/3)
    if x % 2 == 1: return test(2*x+1)

print test(100)



