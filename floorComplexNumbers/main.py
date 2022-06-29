import matplotlib.pyplot as plt

def transformation_floor_b(b: float, c: float, d: float, f: float):
    firstTermReal = -d + b/2

    firstTermImaginary = -f

    # print("Modulus: " + str(((2 * d**2 + b * d + (b**2)/4 - 2 * f ** 2 - c) ** 2 + (4 * d * f + b * f) ** 2 ) ** 0.5))
    # print(2 * d ** 2 + b * d +( b ** 2) / 4 - 2 * f ** 2 - c)

    secondTermReal = round((((((2 * d**2 + b * d + (b**2)/4 - 2 * f ** 2 - c) ** 2 + (4 * d * f + b * f) ** 2 ) ** 0.5) + 2 * d ** 2 + b * d +( b ** 2) / 4 - 2 * f ** 2 - c)/2), 6) ** 0.5

    secondTermImaginary = round((((((2 * d**2 + b * d + (b**2)/4 - 2 * f ** 2 - c) ** 2 + (4 * d * f + b * f) ** 2 ) ** 0.5) + -1 * (2 * d ** 2 + b * d + (b ** 2) / 4 - 2 * f ** 2 - c))/2), 6) ** 0.5

    return ((firstTermReal + secondTermReal, firstTermImaginary + secondTermImaginary), (firstTermReal - secondTermReal, firstTermImaginary - secondTermImaginary))


def main():
    colorValue = 0
    endRange = 10
    increment = 1
    i = 0
    while i < endRange:
        j = 0
        while j < endRange:
            k = 0.0
            while k < 1:
                l = 0.0
                while l < 1:
                    a, b = transformation_floor_b(i, j, k, l)

                    # if (isinstance(a[0], complex)):
                    print((i, j, k, l))
                    #     print(a)
                    if colorValue > 1:
                        colorValue = 1
                    if (a[0].is_integer() and a[1].is_integer()):
                        # print(f"b: {i}, c: {j}, d: {k} = {a[0]} + {a[1]}i")
                        plt.plot(a[0], a[1], marker="o", markersize=1, markeredgecolor=str(colorValue), markerfacecolor=str(colorValue))
                    if (b[0].is_integer() and b[1].is_integer()):
                        # print(f"b: {i}, c: {j}, d: {k} = {b[0]} + {b[1]}i")
                        plt.plot(a[0], a[1], marker="o", markersize=1, markeredgecolor=str(colorValue), markerfacecolor=str(colorValue))
                    l += .1
                k += .1
            colorValue += 1/((endRange/.1) ** 2)
            j += increment
        i += increment
    print("Done")
    plt.show()


if __name__ == '__main__':
    main()