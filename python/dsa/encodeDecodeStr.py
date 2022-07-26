str = ["lintdsklfjelkgjelgk", "code", "love", "you"]
encodedStr = ""
for s in str:
    codeOne = len(s)
    #codeOne = str(codeOneNum)
    codeTwo = "$"
    encodedStr += f'{codeOne}' + codeTwo + s

print(encodedStr)

decodedStr, i = [], 0
while i < len(encodedStr):
    j = i
    while encodedStr[j] != "$":
        j += 1
    length = int(encodedStr[i:j])

    decodedStr.append(encodedStr[j + 1: j + 1 + length])
    i = j + 1 + length

print(decodedStr)
