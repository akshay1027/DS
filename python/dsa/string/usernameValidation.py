def CodelandUsernameValidation(strParam):

    if len(strParam) >= 4 and len(strParam) <= 25 and strParam[0].isalpha() and strParam[- 1] != '_':
        for char in strParam:
            if char.isalnum() == False and char != '_':
                return False
        return True
    else:
        return False


# keep this function call here
print(CodelandUsernameValidation(input()))
