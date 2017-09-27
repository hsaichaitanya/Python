###############################################################################################
# Assume that two variables, varA and varB, are assigned values, either numbers or strings.
#Write a piece of Python code that prints out one of the following messages:
#"string involved" if either varA or varB are strings
#"bigger" if varA is larger than varB
#"equal" if varA is equal to varB
#"smaller" if varA is smaller than varB
################################################################################################

varA = 'Hi i am a string'
varB = 2222222
"""
if varA or varB == type(str):
    print('strings involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print ('equal')
elif varA < varB:
    print('smaller')
else:
    print ('nothing')

"""

if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    print('smaller')