
# method 1
def printNameParams(count: int):
    if count == 5:
        return
    count += 1
    print("Akshay R R params")
    printNameParams(count)


printNameParams(count=0)


# method 2
def printName():
    global count
    if count == 5:
        return

    count += 1
    print("Akshay R R")
    printName()


count = 0
printName()
