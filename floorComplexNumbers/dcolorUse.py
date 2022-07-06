import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import cv2

sys.path.insert(0, './dcolor')

import dcolor
import rgbcolor
from findRoots import getRoots

def main():

    # Objects for plotting
    rc = rgbcolor.DColor()
    dc = dcolor.DColor()

    # Setting variables
    endRange = 2
    b = 1

    # List for storing roots
    roots = []
    
    # Finds roots
    while b < endRange:
        c = 1
        while c < endRange:
            path = rc.plot(lambda z, floor_z: z**2 + b*floor_z + c, metadata=f'z^2 + {b}[z] + {c}') # 
            dc.plot(lambda z, floor_z: z**2 + b*floor_z + c, metadata=f'z^2 + {b}[z] + {c}')
            roots += getRoots(path)
            print(roots)
            c+=.1
        b += .1

    cv2.destroyAllWindows()
    x = [ele.real for ele in roots]
    y = [ele.imag for ele in roots]

    print(x)
    print(y)
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()
    
    plt.scatter(x, y)
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.savefig("./correlation_plot")


if __name__ == "__main__":
    main()