# Remove the repetition from the given string
#       Exp : Abcda
#       Output : Abcd


# Algorithm:
# 1) covert string to lower case
# 2) have a dummy variable to store result
# 3) iterate over string, check if the character in the string is present in the dummy varibale, if not add it

# note:
# 1) 'not in' can only be used for strings and characters

str = input('Enter required string = ').lower()
result = ""

for char in str:
    if char not in result:
        result += char

print(result)
