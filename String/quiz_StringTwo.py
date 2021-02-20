def mask_security_number(security_number):
    string = security_number

    last_index = len(string) - 1
    temp = list(string)

    for i in range(last_index, last_index - 4, -1):
        temp[i] = "*"
    string = ''.join(temp)
    return string


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
