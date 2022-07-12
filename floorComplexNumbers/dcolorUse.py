import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import cv2
import logisticRegr

sys.path.insert(0, './dcolor')

import dcolor
import rgbcolor
from findRoots import getRoots

def main():

    # Setting variables
    endRange = 20

    # Objects for plotting
    rc = rgbcolor.DColor(xmin=-endRange, xmax=endRange, ymin=-endRange, ymax=endRange)
    dc = dcolor.DColor(xmin=-endRange, xmax=endRange, ymin=-endRange, ymax=endRange)

    b = -endRange
    interval = 1

    # List for storing roots
    roots = []
    try:
        # Finds roots
        while b < endRange:
            c = -endRange
            while c < endRange:
                path = rc.plot(lambda z, floor_z: z**2 + b*floor_z + c, metadata=f'z^2 + {b}[z] + {c}') # 
                dc.plot(lambda z, floor_z: z**2 + b*floor_z + c, metadata=f'z^2 + {b}[z] + {c}')
                roots += getRoots(path, endRange)
                plt.figure().clear()
                plt.close()
                plt.cla()
                plt.clf()
                print(roots)
                c+= interval
            b += interval

    finally:
        cv2.destroyAllWindows()
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        thresh = .25

        for ele in roots:
            # if ele.imag < thresh:
            if ele.real > thresh:
                x1.append(ele.real)
                y1.append(ele.imag)
            
            elif ele.real < -thresh:
                x2.append(ele.real)
                y2.append(ele.imag)

        plt.figure().clear()
        plt.close()
        plt.cla()
        plt.clf()
        
        plt.scatter(x1, y1)
        plt.ylabel('Imaginary')
        plt.xlabel('Real')
        # plt.savefig("./correlation_plot")

        plt.scatter(x2, y2)
        plt.ylabel('Imaginary')
        plt.xlabel('Real')

        # regr_func_1 = logisticRegr.loga_regr(x1, y1)
        # regr_func_2 = logisticRegr.loga_regr(x2, y2)

        # xPlot = np.linspace(thresh, 2)

        # plt.plot(xPlot, regr_func_1(xPlot))
        # plt.ylabel('Imaginary')
        # plt.xlabel('Real')

        # xPlot = np.linspace(-thresh, -2)

        # plt.plot(xPlot, regr_func_2(xPlot))
        # plt.ylabel('Imaginary')
        # plt.xlabel('Real')

        plt.savefig("./correlation_plot2")

if __name__ == "__main__":
    main()