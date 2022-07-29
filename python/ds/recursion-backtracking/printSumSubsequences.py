

def printS(index, n, arr, sum, s, ds):
    if index == n:
        if s == sum:
            print(ds)
        return

    s += arr[index]
    ds.append(arr[index])

    printS(index + 1, n, arr, sum, s, ds)

    s -= arr[index]
    ds.pop()

    printS(index + 1, n, arr, sum, s, ds)


arr = [1, 2, 1]
n = len(arr)
sum = 2
ds = []

printS(0, n, arr, sum, 0, ds)


'''    
    Time Complexity : O(2^N)
    Space Complexity : O(N)

    Where N is the number of elements in the array.
'''


def helper(arr, n, k):
    # Base condition.
    if n <= 0:
        # If k = 0, we reached target sum
        if k == 0:
            return 1
        else:
            return 0

    # arr[n-1] not taken in considertion.
    x = helper(arr, n-1, k)
    y = 0

    if(k - arr[n - 1] >= 0):
        # arr[n-1] taken in considertion
        y = helper(arr, n - 1, k - arr[n-1])

    # Return current result
    if x == 1 or y == 1:
        return 1
    else:
        return 0


def subsetSumToK(n, k, arr):
    # Calling recursive function
    ans = helper(arr, n, k)

    if ans == 1:
        return True
    else:
        return False
