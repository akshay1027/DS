
# functional recursion

def printTillNBro(count):
    if count == 0:
        return 0

    return count + printTillNBro(count - 1)


# parameterised recursion

def printTillN(count, sum):
    if count < 1:
        print(sum)
        return

    printTillN(count - 1, sum + count)


print(printTillNBro(3))
printTillN(3, 0)
