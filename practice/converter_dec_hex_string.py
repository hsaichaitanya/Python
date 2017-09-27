def ChangeHex(n):
    x = (n % 16)
    c = ""
    if (x < 10):
        c = x
    if (x == 10):
        c = "A"
    if (x == 11):
        c = "B"
    if (x == 12):
        c = "C"
    if (x == 13):
        c = "D"
    if (x == 14):
        c = "E"
    if (x == 15):
        c = "F"

    if (n - x != 0):
        return ChangeHex(n / 16) + str(c)
    else:
        return str(c)


x = int(input("number is: "))

#converts decimal to hex
y = ChangeHex(x)

#prints out the value
print(ChangeHex(x))





