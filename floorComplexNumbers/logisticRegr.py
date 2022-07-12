import numpy as np
import math

def loga_regr(xVar, yVar):
    fit = np.polyfit(np.log(np.absolute(xVar)), yVar, 1)
    print("fit: " + str(fit))
    return lambda x: fit[0] * np.log(np.absolute(x)) + fit[1]

def test():
    pass

if __name__ == "__main__":
    test()