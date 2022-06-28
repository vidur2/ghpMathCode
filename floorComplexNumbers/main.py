import matplotlib.pyplot as plt
import numpy as np

def transformation_floor_b(b: int, c: int, d: float):
    firstTerm = np.float(b/2)

    secondTerm = ((((b ** 2 - 4 * c + 4 * b * d) ** 2 + 16*b**2) ** np.float(0.5) + b ** 2 - 4*c + 4 * b * d)/2) ** np.float(0.5)

    thirdTerm = ((((b ** 2 - 4 * c + 4 * b * d) ** 2 + 16*b**2) ** np.float(0.5) - b**2 +4*c - 4 * b * d)/2) ** np.float(0.5)

    return (firstTerm + secondTerm, firstTerm - secondTerm, thirdTerm)


def main():

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'k', 'c', 'r', 'k']

    for i in range(-100, 100):
        for j in range(-100, 100):
            k = 0.0
            colorCounter = 0
            while k < 1:
                if round(k, 4) == 1.0:
                    k = 0.9
                else:
                    k = round(k, 4)
                
                print(i, j, k)
                a, b, c = transformation_floor_b(i, j, k)
                color = colors[colorCounter]
                if (a.is_integer() and b.is_integer()):
                    plt.plot(a, b, marker="o", markersize=1, markeredgecolor=color, markerfacecolor=color)
                    plt.plot(a, c, marker="o", markersize=1, markeredgecolor=color, markerfacecolor=color)
                k += .1
                colorCounter += 1
    print("Done")
    plt.show()


if __name__ == '__main__':
    main()