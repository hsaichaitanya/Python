def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to
    #  the result
    while index < len(aTup):
        print aTup
        print index
        rTup = (aTup[index],)
        print rTup
        index += 2
    print rTup
    return rTup


oddTuples((9, 19, 6, 15, 211, 121, 22, 33, 3, 4, 5, 78))

"""

def oddTuples2(aTup):
    '''
    Another way to solve the problem.

    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Here is another solution to the problem that uses tuple
    #  slicing by 2 to achieve the same result
    return aTup[::2]

"""

import warnings; warnings.simplefilter("ignore")
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas
wb_pyth=pd.Excelfile(r"C:\Libraries\Documents\pyth.xlsx")
sheet_1=pd.read_excel(r"C:\Libraries\Documents\pyth.xlsx",sheetname=0)
sheet_2=pd.read_excel(r"C:\Libraries\Documents\pyth.xlsx",sheetname=1)
sheet_3=pd.read_excel(r"C:\Libraries\Documents\pyth.xlsx",sheetname=2)