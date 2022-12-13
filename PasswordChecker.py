password = str(input("Enter password: "))

def CheckPassword(password):

    numsCount = 0
  
    if len(password) < 8:
        print("Password unsafe: less than 8 characters detected.")

    for i in [*password]:
        if i in map(str, range(0, 10)):
            numsCount += 1
            
    if numsCount < 4:
        print("Password unsafe: less than 4 integers detected.")

CheckPassword(password)