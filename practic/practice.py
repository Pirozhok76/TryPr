import math
import sympy
import numpy as np
from fractions import Fraction


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
r2 = 0.5
k1 = 1.4
k2 = 1.33


#M1 = np.array([0.063774118, 0.126879805, 0.178214982])
''' not finished '''

# piks_min = 1.001
# piks_max = 1.121
''' not finished . dpiks = . fpiks = 1.121 '''

# pi0 = 1.1

''' not finished . dpi0 = . fpi0 = 4'''

# rm = 0.5
''' not finished . drm = 0.05 . frm = 1'''

"""
0.063774118
0.126879805
0.178214982
"""


def main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2):


    ''' not finished '''


    #dr = 0.05
    # b = (2 * rm) / ((1 - r2) * ((2 * rm) - r2 - 1))

    # a = -1 * (b / (2 * rm))

    # c = 1 - a - b

    m = (np.log(r2 * (R1 / R2) * (1 / theta2)))

    M1 = np.sqrt(2 * (((piks ** (1 / (k1 - 1) / k1)) - 1) / (k1 - 1)))

    A = ((k1 - 1) / (2 * m)) * (M1 ** 2) / (1 + (1 / Eps ** 2))

    mf1 = M1 / ((1 + (1 / (Eps ** 2))) ** 0.5)

    mz1 = (((M1 ** 2) / (1 + Eps ** 2))**(1/2))

    Fi2 = 1 - A * (1 / ((r2 ** (2 * m)) - 1))

    gamma = ((k1 * (k2 - 1) * z1 * R1) / (2 * k2 * z2 * R2)) * \
            ((M1 ** 2) / ((1 + (1 / Eps ** 2)) * (r2 ** (2 * m)) * theta2 * Fi2) *
             (1 - ((1 / pi0) ** ((k2 - 1) / k2))) * (1 / (Fi2 ** ((k1 * (k2 - 1)) / (k2 * (k1 - 1))))))

    B = (k1 * (k2 - 1) * (M1 ** 2) * z1 * R1) /\
        (2 * k2 * (1 + (1 / (Eps ** 2))) * (r2 ** (2 * m)) * theta2 * Fi2 * z2 * R2)

    mf_vnesh = M1 / ((1 + 1 / Eps ** 2) ** 0.5 * (1 - A * (1 / (r_vnesh ** (2 * m)) - 1)) ** 0.5 * r_vnesh ** (2 * m))

    mf_vnutr = (1/r2 ** m) * ((r_vnutr/r2) ** 2) * (((k1*R1)/(k2*R2)) ** 0.5) * \
               (M1/(((1+(1/Eps ** 2)) ** 0.5) * ((1 - B * (1 - ((r_vnutr / r2) ** (2 * gamma)))) ** 0.5)))

    # _mz = mz1 * (a * (r ** 2) + b * r + c)



    #print(_mz)
    return [M1, list(mz1),
            list(gamma),
            list(mf_vnutr)]



'''def fc():
    calc_a()
    calc_r()
    fi = 1-a*(1/(re2**(2*m))-1)
    print('fi=', fi)
    return'''



'''def calc_theta2():

    global theta2


    while theta2 <= 2:
        theta2 = theta2 + dtheta2
    return
'''
# need finish for:
# m,r2,r,theta2
if __name__ == '__main__':

    main_calc()
   #print(mz1)
    #fc()
