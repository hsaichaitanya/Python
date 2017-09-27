###### steps involved in towers of Hanoi to move in between 3 towers######

def move(fr, to):
    print ('move from ' + str(fr) + 'to' + str(to))

def towers(n, fr, to, spare):
    if n == 1:
        move(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)

print (towers(10, 'P1', 'P2', 'P3'))

"""
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(10, 'P1', 'P2', 'P3'))
"""

