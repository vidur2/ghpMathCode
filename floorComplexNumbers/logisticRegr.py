import numpy as np
import math
from scipy.optimize import curve_fit

def func_powerlaw(x, m, c, c0):
    return c0 + x**m * c

def loga_regr(xVar, yVar):
    x = np.asarray([ 1000, 3250, 5500, 10000, 32500, 55000, 77500, 100000, 200000 ])
    y = np.asarray([ 1100, 500, 288, 200, 113, 67, 52, 44, 5 ])

    sol1, _ = curve_fit(func_powerlaw, x, y, maxfev=2000 )
    # sol2 = curve_fit(func_powerlaw, x, y, p0 = np.asarray([-1,10**5,0]))

    return sol1

def test():
    pass

if __name__ == "__main__":
    test()