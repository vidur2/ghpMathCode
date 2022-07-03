from multiEq import transformation_floor_b
import sys

sys.setrecursionlimit(99999)

def find_integer_solution(prevB, prevC, currentB, currentC):
    b = (prevB + currentB)/2
    c = (prevC + currentC)/2
    a, d = transformation_floor_b(b, c, 0, 0)
    if (int(a[0]) == a[0] and int(a[1] == a[1]) and a[0] != 0 and a[1] != 0) or (int(d[0]) == d[0] and int(d[1]) == d[1] and d[0] != 0 and d[1] != 0):
        print(a, d)
        sys.exit(0)
        return [a, d]
    elif int(a[0]) < a[0] and int(a[1]) < a[1] or int(d[0]) < d[0] and int(d[1]) < d[1]:
        finalC = (prevC + c)/2
        finalB = (prevB + b)/2
        return [find_integer_solution(prevB, prevC, finalB, finalC)]
    elif int(a[0]) > a[0] and int(a[1]) > a[1] or int(d[0]) > d[0] and int(d[1]) > d[1]:
        finalC = (currentC + c)/2
        finalB = (currentB + b)/2
        return [find_integer_solution(finalB, finalC, currentB, currentC)]
    else:
        finalC = (prevC + c)/2
        finalB = (prevB + b)/2
        finalC1 = (currentC + c)/2
        finalB1 = (currentB + b)/2
        return [find_integer_solution(prevB, prevC, finalB, finalC), find_integer_solution(finalB1, finalC1, currentB, currentC)]

def main():
    endNumber = 10
    inc = .1

    prevIntAReal = 0
    prevIntAIm = 0
    prevIntBReal = 0
    prevIntBIm = 0

    i = 0

    while (i < endNumber):
        j = 0
        while (j < endNumber):
            a, b = transformation_floor_b(i, j, 0, 0)

            if int(a[0]) != prevIntAReal and int(a[1]) != prevIntAIm or int(b[0]) != prevIntAReal and int(b[1]) != prevIntAIm:
                find_integer_solution(i - .1, j - .1, i, j)
            prevIntAReal = int(a[0])
            prevIntAIm = int(a[1])
            prevIntBReal = int(b[0])
            prevIntBIm = int(b[1])
            j += inc
        i += inc

if __name__ == "__main__":
    main()
