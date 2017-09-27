#Write a program that uses these bounds and bisection search
#(for more info check out the Wikipedia page on bisection search)
#to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.
#Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!).
#Produce the same return value as you did in Problem 2.

"""
balanceCopy = balance
monthlyInterestRate = annualInterestRate/12
payLowBound = balance/12.0
payHighBound = (balance*((1+monthlyInterestRate)**12))/12.0
minPay = 0

while balance > 0.02 or balance < -0.02:
    balance = balanceCopy
    minPay = (payLowBound + payHighBound)/2
    for i in range(12):
        monthlyUnpaid = balance - minPay
        balance = round(monthlyUnpaid + monthlyInterestRate*monthlyUnpaid,2)
    if balance > 0:
        payLowBound = minPay
    if balance < 0:
        payHighBound = minPay

print "Lowest Payment: "+str(round(minPay,2))

"""