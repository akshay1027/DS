stack = [1]


def push():
    element = input("enter ele to be pushed")
    stack.append(element)
    print(stack, '| ', type(stack))


def pop():
    stack.pop()
    print(stack, '| ', type(stack))


while True:
    choice = int(input("choose operation 1->push | 2->pop | 3->quit"))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("enter any of the given operation")
