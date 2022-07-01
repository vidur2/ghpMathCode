def main():
    # Storage for answers
    answer = 100000
    dividesFrom = 0

    # Iterates through all the possibilities
    for i in range(10000, 100000):

        # Calculates sum of characters
        newI = str(i)
        sumOfChars = 0
        for char in newI:
            sumOfChars += int(char)

        # Stores answer
        if i % sumOfChars == 0 and i/sumOfChars<answer:
            dividesFrom = i
            answer= i/sumOfChars
    
    # Prints out answer of 407 and its quotient
    print(dividesFrom)
    print(answer)


if __name__ == "__main__":
    main()