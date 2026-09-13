
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