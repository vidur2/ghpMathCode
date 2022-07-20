#!/usr/bin/python
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import cv2
import logisticRegr
import gc
import matplotlib

sys.path.insert(0, './dcolor')

import dcolor
import rgbcolor
from findRoots import getRoots

from dataclasses import dataclass

@dataclass
class Root:
    roots: list
    rgba: tuple

def calcRoots(endRange, interval):
    # Objects for plotting
    rc = rgbcolor.DColor(xmin=-endRange, xmax=endRange, ymin=-endRange, ymax=endRange)

    b = -endRange

    # List for storing roots
    roots = []
    try:
        # Finds roots
        while b < endRange:
            c = -endRange
            while c < endRange:
                d = -endRange

                while d < endRange:
                    f = -endRange
                    while f < endRange:
                        path = rc.plot(lambda z, floor_z: z*floor_z+ complex(b, d)*z + complex(c, f), metadata=f'z^2 + ({b} + {d}i)[z] + {c} + {f}i') # 
                        # dc.plot(lambda z, floor_z: z**2 + complex(b, d)*floor_z + complex(c, f), metadata=f'z^2 + ({b} + {d}i)[z] + {c} + {f}i')
                        roots.append(Root(getRoots(path, endRange), ((endRange - b)/(3*endRange), (endRange - c)/(3*endRange), (endRange - d)/(3*endRange), (endRange - f)/(3*endRange))))
                        plt.close()
                        plt.figure().clear()
                        plt.cla()
                        plt.clf()
                        print(roots)
                        f += interval
                    d += interval
                c+= interval
            b += interval

    finally:
        cv2.destroyAllWindows()
        x1 = []
        y1 = []
        # x2 = []
        # y2 = []
        thresh = .25

        plt.figure().clear()
        plt.close()
        plt.cla()
        plt.clf()

        for ele in roots:
            x1 = [subele.real for subele in ele.roots]
            y1 = [subele.imag for subele in ele.roots]
            print(ele.rgba)
            plt.scatter(x1, y1, color=ele.rgba)
            x1=[]
            y1=[]
        # plt.scatter(x1, y1)
        plt.ylabel('Imaginary')
        plt.xlabel('Real')
        plt.savefig("./final_correlation.png")
        # plt.scatter(x1, y1)
        # plt.savefig("./correlation_plot")
        # regr_func_1 = logisticRegr.loga_regr(x1, y1)
        # regr_func_2 = logisticRegr.loga_regr(x2, y2)

        # xPlot = np.linspace(thresh, 2)

        # plt.plot(xPlot, regr_func_1(xPlot))
        # plt.ylabel('Imaginary')
        # plt.xlabel('Real')

        xPlot = np.linspace(-thresh, -2)

        # plt.plot(xPlot, func_powerlaw(xPlot, regr_func_1[0], regr_func_1[1], regr_func_1[2]))
        # plt.ylabel('Imaginary')
        # plt.xlabel('Real')

        f = open("./data/zZfloorzFloorbz.txt", "a")
        f.truncate(0)

        for line in x1:
            f.write("%s\n" % line)

        f.write("\n\n")
        
        for line in y1:
            f.write("%s\n" % line)

        f.close()

def main():

    # Setting variables
    endRange = 3
    interval = 1

    calcRoots(endRange, interval)

if __name__ == "__main__":
    main()
