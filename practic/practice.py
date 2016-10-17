import math
import sympy
import numpy as np
from fractions import Fraction

#Eps = [Fraction(0.577), Fraction(1), Fraction(1.732), Fraction(3.732), Fraction(11.43)]

Eps = np.array([Fraction(0.577), Fraction(1), Fraction(1.732), Fraction(3.732), Fraction(11.43)])

"""Eps[1] = Fraction(0.577)
Eps[2] = Fraction(1)
Eps[3] = Fraction(1.732)
Eps[4] = Fraction(3.732)
Eps[5] = Fraction(11.43)"""

R2 = 288.3
R1 = 287
z1 = 1
z2 = 1
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

    dr = 0.05
    r = r2
    while r <= 1:
        r = r2 + dr
    return


def calc_a():
    global a

    a = ((k1-1)/(2*m))*(M1**2)/(1+(1/Eps**2))
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
        m1 = np.sqrt(2*(((piks**(1/(k1-1)/k1))-1)/(k1-1)))
        #em1 = [m1]
        piks += 0.001
    return


def calc_mf1():
    calc_m1()
    mf1 = m1/((1+(1/(Eps**2)))**0.5)
    print(mf1)
    return


def calc_mz1():
    global mz1
    calc_m1()
    mz1 = np.sqrt((m1**2)/(1+Eps**2))
    return


def calc_theta2():

    global theta2
    dtheta2 = 0.1
    theta2 = 1
    while theta2 <= 2:
        theta2 = theta2 + dtheta2
    return


def calc_m():
    global m
    m = (np.log(r2*(R1/R2)*(1/theta2)))

    return


def calc_mf_vnesh():
    mf_vnesh = M1/((1+1/Eps**2)**0.5*(1-a*(1/(r**(2*m))-1))**0.5*r**(2*m))
    return

if __name__ == '__main__':
    calc_mf_vnesh()
   #print(mz1)
    #fc()
