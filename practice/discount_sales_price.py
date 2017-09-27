#priginal price
#discount = 20%
#price after discount
#sales price


def discount(x):
    return (x/100)

originalprice = int(input('enter a price= '))
x = int(input('how much discount: '))
y = originalprice - (originalprice*discount(x))
print ('sales price is : ', str(y))



