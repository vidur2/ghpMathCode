import sys

sys.path.insert(0, './dcolor')

import dcolor

endRange = 8
dc = dcolor.DColor(xmin=-endRange, xmax=endRange, ymin=-endRange, ymax=endRange)

path = dc.plot(lambda z, floor_z: z, metadata=f'z')

print(path)