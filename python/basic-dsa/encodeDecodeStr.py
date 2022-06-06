str = ["lintdsklfjelkgjelgk", "code", "love", "you"]
encodedStr = ""
for i in range(len(str)):
    codeOne = len(str[i])
    #codeOne = str(codeOneNum)
    codeTwo = "$"
    tempStr = f'{codeOne}' + codeTwo + str[i]
    encodedStr += tempStr
print(encodedStr)


decodedStr, i = [], 0
while i < len(str):
    j = i
    while encodedStr[j] != "$":
        j += 1
    length = int(str[i:j])

    decodedStr.append(encodedStr[j + 1: j + 1 + length])
    i = j + 1 + length
print(decodedStr)
