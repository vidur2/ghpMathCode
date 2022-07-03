import math

def floor_complex(a):
    return complex(math.floor(a.real), math.floor(a.imag))

def get_plugin_complex_roots(root, b):
    c = -root**complex(2, 0)- b * floor_complex(root)

    if c.imag == 0 and root.imag != 0 and root.real != 0:
        print(f"root: {root} from x^2 + {b}[x] + {c}")

def main():
    endRange = 10
    for i in range(-endRange, endRange):
        for j in range(-endRange, endRange):
            for k in range(-endRange, endRange):
                get_plugin_complex_roots(complex(j, k), complex(i, 0))

if (__name__ == "__main__"):
    main()