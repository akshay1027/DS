def check(s):
    hash = {}

    for char in s:
        hash[char] = hash.get(char, 0) + 1

    for char in hash:
        if hash[char] > 1:
            print(f"'{char}' occurs {hash[char]} times")


# Driver Code
if __name__ == '__main__':

    s = "test string"

    check(s)
