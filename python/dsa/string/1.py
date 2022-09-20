
def maxLength(strings):
    maxLen = 0
    uniqueElements = set()

    ind = 0
    for string in strings:
        ind += 1
        localMax = 0
        for char in string:
            if ind == 1:
                if char not in uniqueElements:
                    uniqueElements.add(char)
                    localMax += 1
                else:
                    maxLen = max(maxLen, localMax)
                    localMax = 0
            else:
                if char in uniqueElements:
                    localMax = 0
                    break
                else:
                    localMax += 1

        print(localMax)
        if ind == 1:
            maxLen = max(maxLen, localMax)
        else:
            maxLen += localMax

    return maxLen


# Driver Code
if __name__ == '__main__':

    s = ["ab", "cd", "ab"]
    # s = []
    # s.append("abcadefgh")
    # s.append("xyzaq")

    print(maxLength(s))
