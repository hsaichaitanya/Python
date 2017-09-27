"""
#######fourth power############
def fourthPower(x):
    '''
    x: int or float.
    '''
    def square(x):
        return x*x
    return square(square(x))

#########odd number##########
def odd(x):
    if (x%2) == 0:
        print ("x is even")
    else:
        print ("x is odd")
    return (x%2==0)

odd(20)
#################exponential fn##############
def iterPower(base, exp):
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

print (iterPower(2,3))

###################iteration###################
if exp <= 0:
    return 1
return base * recurPower(base, exp - 1)"""
################################################
"""
def gcd(a, b):
    while (a!=b):
        if a > b:
            a = a-b
        else:
            b = b-a
        return a

print(gcd (10,12))
"""

future_value=float(input('10000'))
rate=float(input('1.23'))
years=float(input('10'))
present_value=future_value/(1+1.23)**10
print('you will need to deposit',present_value)