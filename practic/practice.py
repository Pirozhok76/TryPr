import math
import sympy
import numpy as np
from fractions import Fraction

Eps = np.array([Fraction(0.577), Fraction(1), Fraction(1.732), Fraction(3.732), Fraction(11.43)])

R2 = 288.3
R1 = 287
z1 = 1
z2 = 1
r2 = 0.5
k1 = 1.4
k2 = 1.33


# M1 = np.array([0.063774118, 0.126879805, 0.178214982])



def main_calc(piks, pi0, theta2, r_vnesh, r_vnutr, r2, eps):
    ''' not finished '''

    # b = (2 * rm) / ((1 - r2) * ((2 * rm) - r2 - 1))

    # a = -1 * (b / (2 * rm))

    # c = 1 - a - b

    m = (np.log(r2 * (R1 / R2) * (1 / theta2)))

    M1 = np.sqrt(2 * (((piks ** (1 / (k1 - 1) / k1)) - 1) / (k1 - 1)))

    A = ((k1 - 1) / (2 * m)) * (M1 ** 2) / (1 + (1 / eps ** 2))

    mf1 = M1 / ((1 + (1 / (eps ** 2))) ** 0.5)

    mz1 = (((M1 ** 2) / (1 + eps ** 2)) ** (1 / 2))

    Fi2 = 1 - A * (1 / ((r2 ** (2 * m)) - 1))

    gamma = ((k1 * (k2 - 1) * z1 * R1) / (2 * k2 * z2 * R2)) * \
            ((M1 ** 2) / ((1 + (1 / eps ** 2)) * (r2 ** (2 * m)) * theta2 * Fi2) *
             (1 - ((1 / pi0) ** ((k2 - 1) / k2))) * (1 / (Fi2 ** ((k1 * (k2 - 1)) / (k2 * (k1 - 1))))))

    B = (k1 * (k2 - 1) * (M1 ** 2) * z1 * R1) / \
        (2 * k2 * (1 + (1 / (eps ** 2))) * (r2 ** (2 * m)) * theta2 * Fi2 * z2 * R2)

    if r_vnesh is not None:
        mf_vnesh = M1 /\
                   ((1 + 1 / eps ** 2) ** 0.5 * (1 - A * (1 / (r_vnesh ** (2 * m)) - 1)) ** 0.5 * r_vnesh ** (2 * m))
        return mf_vnesh

    if r_vnutr is not None:
        mf_vnutr = (1 / r2 ** m) * ((r_vnutr / r2) ** 2) * (((k1 * R1) / (k2 * R2)) ** 0.5) * \
                   (M1 / (((1 + (1 / eps ** 2)) ** 0.5) * ((1 - B * (1 - ((r_vnutr / r2) ** (2 * gamma)))) ** 0.5)))
        return mf_vnutr

    # _mz = mz1 * (a * (r ** 2) + b * r + c)


'''def fc():
	calc_a()
	calc_r()
	fi = 1-a*(1/(re2**(2*m))-1)
	print('fi=', fi)
	return'''

if __name__ == '__main__':
    main_calc()
    # print(mz1)
# fc()
