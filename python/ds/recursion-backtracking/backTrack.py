# backtracking is thinking in reverse, that is, printing after recursion call.
# normal recursion, we print before recursion call


# print 1 to n using backtracking

def backTrack(i):
    if i < 1:
        return
    backTrack(i-1)
    print(i)


backTrack(3)


# print n to 1 using backtracking

def backTrack(i, n):
    if i > n:
        return
    backTrack(i+1, n)
    print(i)


backTrack(1, 3)
