import math
import sympy
import numpy as np
import array
from fractions import Fraction

Eps = []
Eps[1] = Fraction(0.577)
Eps[2] = Fraction(1)
Eps[3] = Fraction(1.732)
Eps[4] = Fraction(3.732)
Eps[5] = Fraction(11.43)


#Eps = Fraction(0.577, 1.0, 1.732, 3.732, 11.43)


r2 = 0.7
k1 = 1.4
m = 1
M1 = np.array([0.063774118, 0.126879805, 0.178214982])

"""
0.063774118
0.126879805
0.178214982
"""


def calc_r():
    global re2
    dr = 0.05
    re2 = r2
    while re2 < 1:
        re2 = r2 + dr
    return


def calc_a():
    global a
    a = ((k1-1)/(2*m))*(M1**2)/(1+(1/Eps**2))
    print('res =', a)
    return


'''def fc():
    calc_a()
    calc_r()
    fi = 1-a*(1/(re2**(2*m))-1)
    print('fi=', fi)
    return'''


def calc_m1():
    global m1
    piks = 1.001
    while 1.001 <= piks <= 1.121:
        m1 = math.sqrt(2*(((piks**(1/(k1-1)/k1))-1)/(k1-1)))
        #em1 = [m1]
        piks += 0.001

       # print('m1 =', m1)
    return


def calc_mf1():
    calc_m1()
    mf1 = m1/((1+(1/(Eps**2)))**0.5)
    print(mf1)
    return


def calc_mz1():
    global mz1
    calc_m1()
    mz1 = math.sqrt((m1**2)/(1+Eps**2))
    return


def calc_m():
    np.log()

    return


if __name__ == '__main__':
    calc_mz1()
   #print(mz1)
    #fc()
