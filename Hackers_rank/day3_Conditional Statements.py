#!/bin/python3

import sys


#N = int(input().strip(" "))
N = int(input())
ans = 'Weird'

if N % 2 == 0 and not 6 <= N <= 20:
    ans = 'Not ' + ans

else:
    ans = 'Weird'

print ans