password = str(input("Enter password: "))

def CheckPassword(password):

    numsCount = 0
    upperCases = 0

    #Check for password's length
    if len(password) < 8:
        print("Password unsafe: less than 8 characters detected.")

    #Check for integers inside the password
    for i in [*password]:
        if i in map(str, range(0, 10)):
            numsCount += 1

    if numsCount < 4:
        print("Password unsafe: less than 4 integers detected.")

    #TODO: Check for capitalisation in password
    for i in [*password]:
        if i.isupper():
            upperCases += 1
    if upperCases < 3:
        print("Password unsafe: less than 3 capitalised characters detecetd")
    

CheckPassword(password)