import matplotlib.pyplot as plt
import numpy as np

def transformation_floor_b(b: int, c: int, d: float):
    firstTerm = np.float(b/2)

    secondTerm = ((((b ** 2 - 4 * c + 4 * b * d) ** 2 + 16*b**2) ** np.float(0.5) + b ** 2 - 4*c + 4 * b * d)/2) ** np.float(0.5)

    thirdTerm = ((((b ** 2 - 4 * c + 4 * b * d) ** 2 + 16*b**2) ** np.float(0.5) - b**2 +4*c - 4 * b * d)/2) ** np.float(0.5)

    return (firstTerm + secondTerm, firstTerm - secondTerm, thirdTerm)


def main():
    colorValue = 0
    endRange = 100
    for i in range(0, endRange):
        for j in range(0, endRange):
            k = 0.0
            while k < 1:
                if round(k, 4) == 1.0:
                    k = 0.9
                else:
                    k = round(k, 4)
                a, b, c = transformation_floor_b(i, j, k)
                if (a.is_integer() and b.is_integer()):
                    plt.plot(a, b, marker="o", markersize=1, markeredgecolor=str(colorValue), markerfacecolor=str(colorValue))
                    plt.plot(a, c, marker="o", markersize=1, markeredgecolor=str(colorValue), markerfacecolor=str(colorValue))
                k += .01
            colorValue += 1/(endRange ** 2)
            print(colorValue)
    print("Done")
    plt.show()


if __name__ == '__main__':
    main()