b = float(input('balance = '))
r = float(input('annualInterestRate = '))
c = float(input('monthlyPaymentRate = '))
n = 0   # no of months

for i in range(12)
    mp = (b*c)  #minimum payment
    up = round((b - mp), 2)  #unpaid amount
    b =
        # i = ((r/12.0) * up)    #interest
    n += 1
    print ('Month', n, 'Remaining balance: ', up)

"""
monthlyInterestRate = annualInterestRate/12
totalPaid = 0

for i in range(12):
    minPay = monthlyPaymentRate*balance
    monthlyUnpaid = balance - minPay
    balance = monthlyUnpaid + monthlyInterestRate*monthlyUnpaid
    totalPaid += minPay
    print "Month: "+str(i+1)
    print "Minimum monthly payment: "+str(round(minPay,2))
    print "Remaining balance: " + str(round(balance,2))
    

print "Total paid: "+str(round(totalPaid,2))
print "Remaining balance: "+str(round(balance,2))
"""