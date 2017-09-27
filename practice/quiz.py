"""# Paste your function here
def print_without_vowels(s):
    new=[]
    vowels = ("aeiouAEIOU")
    for i in s:
        if i not in vowels:
            new.append(i)
    print (new)
    #return ''.join(new)


def print_without_vowels(s):
    newstring=""
    for i in s:
        if i not in "aeiouAEIOU":
            newstring=newstring+i
    s=newstring
    print (s)

print_without_vowels('hi i am chaitan')



def largest_odd_times(L):
    m = []
    for x in L:
        if x % 2 == 1:
            m.append(x)
    return max(m)
"""


"""
odd_nums = []
for i in xrange(10):
    value = int(raw_input('Enter an integer: '))
    if value % 2 != 0:
        odd_nums.append(value)

if len(odd_nums) != 0:
    print max(odd_nums)
else:
    print "No odd values"
############################################
def largest_odd_times(L):
    #m = []
    n = L[1::2]
    if len(L) > 2:
        print max(n)
    elif len(L) < 2:
        print max(L)
    else:
        print("None")

    #print max(n)

largest_odd_times([3, 2])
largest_odd_times([3, 0, 5, 3, 5])
largest_odd_times([3, 9, 5, 3, 5, 3])

"""
##########################################
d = {3: 'bear', 1: 'crocodile', 2: 'kangaroo', 0: 'goat'}
print(d)
# Invert d
t = {v: k for k, v in d.items()}
# Copy t to d
d.clear()
d.update(t)
# Remove t
del t
print(d)

###########################
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    inv_map = {}
    for k, v in d.iteritems():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
        inv_map[v] = sorted(inv_map[v])
    print (inv_map)
    return inv_map

dict_invert({3: 'bear', 1: 'crocodile', 2: 'kangaroo', 0: 'goat'})

