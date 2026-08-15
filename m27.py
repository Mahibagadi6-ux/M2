"""fruits = {
    "apple" : 1,
    "banana" : 2,
    "mango" : 3,
    "orange" : 4,
}
fruits["grapes"] = "9"
fruits["banana"] = "10"
print(fruits)

del fruits["banana"]
print(fruits)

print(fruits.items())

d = {
    "friend_1" : {
        "name" : " mahesh",
        "fav_food" : "biriyanui",
        "fav_sport":"cricket",
        "fav_hero":"rocky"
    },
    "friend_2": {
        "name" : "vishwa",
        "fav_food" : "chicken",
        "fav_sport" : "batmiten",
        "fav_hero" : "rocky_bhai"
    }

}
f = d["friend_1"]
print(f["fav_food"])


age  = int(input("enter your age: "))
if age < 18:
    print("you are age is too young")
elif age < 50:
    print("you are the young u must take is the buss ticket")
elif age >= 50:
    print("you  are the old so you get the disscount")
else:
    print("no entry in the bus   ")

time = int(input("enter your time: "))
if time ==8:
    print("break fast")
elif time ==1:
    print("lunch time")
elif time == 20:
    print("it`s dinner time")
else:
    print("working time")

age = int(input("enter your age: "))
if age < 18:
    print("you get the student membership ")
elif age >= 60:
    print("you get the senior citizen membership")
else:
    print("your not eligible for that ")



i = 1
while i <= 10:
    print(i)
    i = i + 1
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i,end=" ")
    i = i + 1
print(i)

seats = 8
while seats > 0:
    print("booked one seat")
    seats = seats - 1
    print( "remain setas ",seats)
else:
    print("no more setas ")

import time
i = 10
while i > 0:
    print("count number " ,end= " ")
    time.sleep(1)
    i = i - 1
    print( i)


else:
    print(" happy new year ")"""


for i in range(1,10):
    if i % 2 == 0:
        print(i)



for i in range(1,10):
    if i % 2 != 0:
        print(i)

total = 0
for i in range(1,11):
    total = total + i
print(total)


vowels = 'aeiou'
name = "mahesh"
count = 0
for i in name:
    if i in vowels:
        count = count + 1
print(count)

name = "this is mahesh"
for i in name:
    if i in vowels:
        print(i,end=" ")







