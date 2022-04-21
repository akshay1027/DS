queue = [1, 2, 3]


def enqueue():
    element = input('enter ele = ')
    queue.append(element)


def dequeue():
    queue.pop(0)


while True:
    choice = int(input('enter the choice, 1. Push | 2. Pop | 3. Quit = '))

    if choice == 1:
        enqueue()
        print(queue)

    elif choice == 2:
        dequeue()
        print(queue)

    elif choice == 3:
        break

    else:
        print('Wrong choice')
