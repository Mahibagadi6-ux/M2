# if and else

name = (input("Enetr the name : "))
passwprd = (input("Enetr the password : "))

if name == "mahesh" and passwprd == "123456":
    print("open the screen lock")
else:
    print("close the screen ")


#if ,else, elife
age = int(input("Enetr the age : "))
if age < 18:
    print(" you are not capable to vote ")
elif age >=18:
    print(" you are capable to vote")
else:
    print("  you dont have voter id so you are not capable to vote")
gender = input("Enetr the gender : ")
age = int(input("Enetr the age : "))
if gender == "female" and  age < 18:
    print("bus ticket is free")
else:
    if gender == "male" and   age < 18:
        print("buss ticket ticket is free")
    elif gender == "male" and  age <= 40:
        print("you pay half ticket")
    elif gender == "male" and age > 40:
        print("ticket is free")


day = input("Enetr the day : ")
is_raining = True
if day == "sunday" or  day=="saturday":
   if not is_raining :
       print("lets go go play")
   else:
       print("stay in home" )

else:
    print("wait untill rains stop or wait for the weekend")

n1 = int(input("Enetr the number  : "))
n2 = int(input("Enetr the number  : "))
n3 = int(input("Enetr the number  : "))
if n1 > n2 and n1 > n3:
    print("n1 is gretar than n2 and n3")
elif n2 > n1 and n2 > n3:
    print("n2 is gretar than n1 and n3")
else:
    print("n3 is greater than n1 and n2")

marks = int(input("Enetr the marks : "))
if marks >80 and marks <=100:
    print("congrats you get A grade")
elif marks > 65 and marks <=80:
    print("congrats you get B grade")
elif marks > 50 and marks <=65:
    print("congrats you get C grade")
else:
    print("sorry you are fail")


