#A regular polygon has n number of sides. Each side has length s.
#The perimeter of a polygon is: length of the boundary of the polygon
#Write a function called polysum that takes 2 arguments, n and s.
# This function *** {{{{   should sum the area and square of the perimeter of the regular polygon. }}} ***
# The function returns the sum, rounded to 4 decimal places.
#{0.25*n*s^2}/{tan(pi/n)}

from math import tan, pi

def polysum(n,s):
    a =  0.25 * n * s * s
    b =  tan(pi / n)
    p_area = round(a/b, 4)
    #print("The area of the polygon is: ", p_area)
    #print(p_area)
    perim = n * s
    area = (perim**2) + p_area
    print area
    return area

polysum(88,90)
"""
import math
def area(n, s):
    area = n*s*s / (4 * math.tan(math.pi/n))
    print area
    return area

area(88, 90)



#Test: polysum(88, 90)
#my : 4989487.55594075
# 67715887.5559
"""