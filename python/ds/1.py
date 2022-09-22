n = int(input())
s = input()

buff, x, cv = s[0], 1, 1
for i in range(1, n):
    if buff == s[i]:
        cv += 1
    else:
        x *= cv
        cv, buff = 1, s[i]
print(x*cv)
