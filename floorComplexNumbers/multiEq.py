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
    increment = .1
    i = 0
    colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')

    while i < endRange:
        j = 0
        while j < endRange:
            k = 0.0
            # while k < 1:
                # l = 0.0
            colorIndex = 0
                # while l < 1:
            a, b = transformation_floor_b(i, j, 0, 0)

            # if (isinstance(a[0], complex))
            #     print(a)
            if (a[0].is_integer() and a[1].is_integer):
                if (not a[1].is_integer() and i != 0):
                    print((i, j, a[1]))
                colorValue = colors[colorIndex % (len(colors) - 1)]
                # print(f"b: {i}, c: {j}, d: {k} = {a[0]} + {a[1]}i")
                plt.plot(a[0], a[1], marker="o", markersize=1, markeredgecolor=str(colorValue), markerfacecolor=str(colorValue))
            if (b[0].is_integer() and b[1].is_integer):
                if (not b[1].is_integer() and i != 0):
                    print(i, j, (b[1]))
                # print(f"b: {i}, c: {j}, d: {k} = {b[0]} + {b[1]}i")
                plt.plot(b[0], b[1], marker="o", markersize=1, markeredgecolor=str(colorValue), markerfacecolor=str(colorValue))
                colorIndex += 1
                    # l += .1
                # k += .1

            j += increment
        i += increment
    print("Done")
    plt.show()


if __name__ == '__main__':
    main()