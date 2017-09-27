"""
Determine if the given number is a power of some non-negative integer.

Example

For n = 125, the output should be
isPower(n) = true;
For n = 72, the output should be
isPower(n) = false.
Input/Output

[time limit] 4000ms (py3)
[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 400.

[output] boolean

true if n can be represented in the form ab (a to the power of b) where a and b are some non-negative integers and b ≥ 2, false otherwise.

Int I=2
"""
import random


class coin:
    def __int__(self):
        self.sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup


def main():
    my_coin = coin()
    print('the side is up', my_coin.get_sideup())
    print('i am tossing the coin')
    my_coin.toss()
    print('the side is up', my_coin.get_sideup())


main()





