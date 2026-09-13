#match case statement
num  = int(input("Enter a number: >>"))
match num:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case _:
        print("print some other number")
day = input("Enter the day: ".lower())
match day:
    case "monday":
        print("work day")
    case "tuesday" | "wednesday":
        print("week middle days")
    case "thursday" | "friday" | "saturday":
        print("almost weekend")
    case "saturday" | "sunday":
        print("weekend")
    case _:
        print("other week day")

time = int(input("Enter the time: "))
match time:
    case 8:
        print("break fast time ")
    case 9:
        print(" want to go to the collage ")
    case 10:
        print("class listion time ")
    case 11:
        print("small break time  ")
    case 12 | 13:
        print(" rest time")
    case _:
        print("study time ")