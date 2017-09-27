ef ispalindrome(x):

    def tochars(x):
        x = x.lower()
        ans = ''
        if s in x:
            if s in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + s
            return ans
    def ispal(x):
        if len(x) <= 1:
            return True
        else:
            return x[0] == x[-1] and ispal(x[1:-1])

    return ispal(tochars(x))


print("")
print ('is eve a palindrome?')
print (ispalindrome('eve'))

print ('')
print ('is able was i ere i saw elba a palindrome')
print (ispalindrome('able was i,ere i saw  elba'))


