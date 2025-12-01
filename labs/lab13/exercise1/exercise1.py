correct_password = "python123"
attemps = 0 

while attemps < 3 : 
    password = input("Enter password : ")
    attemps = attemps + 1

    if password == correct_password : 
        login_successful = "Login accessed!"
        attempts_used = attemps
        break
    else : 
        login_successful = "not successful"
        attempts_used = attemps

print(login_successful)
print("attemps:",attempts_used)
