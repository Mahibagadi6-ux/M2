fruits = {
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