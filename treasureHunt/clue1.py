def main():
    clue = b"NLITZMWVHP"

    minPoint = min(clue)

    relDiff = []

    for char in clue:
        relDiff.append(char - minPoint)

    for i in range(27):
        localDiff = []
        
        for j in relDiff:
            localDiff.append((i + j) % 26 + 65)
        
        print(f"{i}: {str(bytes(localDiff))}")



if __name__ == "__main__":
    main()