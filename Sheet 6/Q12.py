while True: 
    password = input("Enter a password: ")
    if len(password) >= 8:
        print("New Password accepted")
        break
    else:
        print("Weak password. Password should have 8 or more characters. Please try again.")