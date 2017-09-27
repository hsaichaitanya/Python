#############################################################################################################################
# Assume s is a string of lower case characters.Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print Number of times bob occurs is: 2
##############################################################################################################################
s = 'hi bob i am chaitan. Bob is BOB and bob'

"""
c='bob'
total = 0
for c in s:
    if c == 'bob':
        print "number of times bob: " + str(total)
        total += 1
    else:
        print "none"
###########################################################
"""
a = 'bob'
result = 0
numBOB = 0
sub_len = len(a)
for i in range(len(s)):
    if s[i:i+sub_len] == a:
        print s[i:i+sub_len]
        result += 1
print ('Number of times bob occurs is:', result)

############################################################
"""
print(len(s))
for i in range(len(s)):
    s[0:3]
"""


