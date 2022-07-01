from multiEq import transformation_floor_b
import matplotlib.pyplot as plt

def main():
    k = 0.0
    i = 1
    j = 1
    colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
    while k < 1:
        l = 0.0
        colorIndex = 0
        while l < 1:
            a, b = transformation_floor_b(i, j, k, l)

            # if (isinstance(a[0], complex))
            #     print(a)
            if (k != 0 or l != 0):
                colorValue = colors[colorIndex % (len(colors) - 1)]
                # print(f"b: {i}, c: {j}, d: {k} = {a[0]} + {a[1]}i")
                plt.plot(a[0], a[1], marker="o", markersize=1, markeredgecolor='k', markerfacecolor=str(colorValue))
                # print(f"b: {i}, c: {j}, d: {k} = {b[0]} + {b[1]}i")
                plt.plot(b[0], b[1], marker="o", markersize=1, markeredgecolor='k', markerfacecolor=str(colorValue))
                colorIndex += 1
            else:
                print(f"b: {i}, c: {j}, d: {k} = {a[0]} + {a[1]}i")
                plt.plot(a[0], a[1], marker="o", markersize=1, markeredgecolor='r', markerfacecolor='r')
                print(f"b: {i}, c: {j}, d: {k} = {b[0]} + {b[1]}i")
                plt.plot(b[0], b[1], marker="o", markersize=1, markeredgecolor='r', markerfacecolor='r')
            l += .1
        k += .1
    
    # plt.show()


if __name__ == "__main__":
    main()