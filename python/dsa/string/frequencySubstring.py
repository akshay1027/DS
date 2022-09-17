

# bro1 = "tim"
# str1 = "TimisplayinginthehouseoftimwitHthetim"
bro1 = "ak"
str1 = "akshaky"

str = str1.lower()
bro = bro1.lower()

print(str, bro)
localCount = 0
res = 0

l1 = len(bro)

i, j = 0, 0

while i < len(str):
    while l1 and i < len(str):
        if bro[j] == str[i]:
            localCount += 1
        else:
            break

        i += 1
        j += 1
        l1 -= 1

    j = 0
    i += 1
    l1 = len(bro)

    if localCount == l1:
        res += 1

    localCount = 0

print(res)
