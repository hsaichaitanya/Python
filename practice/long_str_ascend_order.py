################################################################################################################
# Assume s is a string of lower case characters.Write a program that prints the longest substring of s in which
#the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc
################################################################################################################
s='llthkevjudmwjrort'
newstr = s[0]
long = s[0]
for i in range(1, len(s)):   #i=[1,2,3,...len(s)-1]
    if s[i] >= newstr[-1]:    #comparing first and last term
        newstr += s[i]        #increment
        if len(newstr) > len(long):
            long = newstr
    else:
        newstr = s[i]
print 'Longest substring in alphabetical order is: ', long


