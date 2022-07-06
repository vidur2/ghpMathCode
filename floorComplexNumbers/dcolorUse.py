import sys
import math
import numpy as np

sys.path.insert(0, './dcolor')

import dcolor
import rgbcolor
from findRoots import getRoots

def main():
    rc = rgbcolor.DColor()
    dc = dcolor.DColor()
    endRange = 2
    b = 1
    roots = []
    
    while b < endRange:
        c = 1
        while c < endRange:
            path = rc.plot(lambda z, floor_z: z**2 + b*floor_z + c, metadata=f'z^2 + {b}[z] + {c}') # 
            dc.plot(lambda z, floor_z: z**2 + b*floor_z + c, metadata=f'z^2 + {b}[z] + {c}')
            roots += getRoots(path)
            print(roots)
            c+=.1
        b += .1

if __name__ == "__main__":
    main()