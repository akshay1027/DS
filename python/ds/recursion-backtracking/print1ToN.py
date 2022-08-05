

n = int(input("Enter N"))


def printTillN(count, n):
    if count == n+1:
        return

    # count += 1
    print(count)
    printTillN(count + 1, n)


def printReverseTillN(count, n):
    if count == n-1:
        return

    print(count)
    printReverseTillN(count - 1, n)


printTillN(1, n)
printReverseTillN(5, 1)
