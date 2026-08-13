# nested if number 1
nu1 = int(input("Enetr the marks : "))
if nu1>10:
    print("nu1 is greater than 10")
    if nu1>100:
        print("nu1 is greater than 100")
    else:
        print("nu1 not greater than 100")

#numbwr 2
age = int(input("Enetr the age : "))
has_license = True
if age>=18:
    if has_license:
        print("you can drive")
    else:
        print("you cannot drive")
else:
    print("you cannot drive too young ")



score = int(input("Enetr the score : "))
attendence = int(input("Enetr the attendence : "))
assigment_sub = True
if score>=65:
    if attendence>=80:
        if assigment_sub:
            print("you got good graid ")
        else:
            print("you not submit the assigment ")
    else:
        print("pass but low attendence ")
else:
    print("fail")


username = input("Enetr the username : ")
password = input("Enetr the password : ")
is_active = True
if username == "mahibagadi":
    if password == "1234567":
        if is_active:
            print("you are logged in")
        else:
            print("account is   not active ")
    else:
        print("password is not correct")
else:
    print("username is incorrect ")
