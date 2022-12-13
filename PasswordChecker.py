password = str(input("Enter password: "))

def CheckPassword(password):

    passwordList = [*password]
    numsCount = 0
    upperCases = 0
    specialChars = 0
    unsafeCount = 0
    safeCount = 0
    j = 0

    #Check for password's length
    if len(password) < 8:
        print("!! Password unsafe: less than 8 characters detected. !!")
        unsafeCount += 1
    else:
        safeCount += 1

    #Check for integers inside the password
    for i in passwordList:
        if i in map(str, range(0, 10)):
            numsCount += 1

    if numsCount < 4:
        print("!! Password unsafe: less than 4 integers detected. !!")
        unsafeCount += 1
    else:
        safeCount += 1

    #Check for capitalisation in password
    for i in passwordList:
        if i.isupper():
            upperCases += 1
    if upperCases < 3:
        print("!! Password unsafe: less than 3 capitalised characters detected !!")
        unsafeCount += 1
    else:
        safeCount += 1

    #Check for special characters
    while j < len([*password]):
       
        if passwordList[j].upper() == passwordList[j] and passwordList[j] not in range(0, 10):
            specialChars += 1
        j += 1

    if specialChars < 1:
        unsafeCount += 1
        print("!! Password unsafe: no special characters detected. !!")
    else:
        safeCount += 1

    print(f"------------ Safety percentage: {int((safeCount / 4) * 100)}% ------------" )
    

CheckPassword(password)