def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def display_menu():
    print("##  simple calculater   ")
    print("1.add\n2.sub\n3.mul\n4.div\n5.exite")
while True:
    display_menu()
    choice = int(input("Enter choice:"))
    if choice in {1, 2, 3, 4, 5}:
        a = float(input("Enter first number:"))
        b = float(input("Enter second number:"))
    if choice == 1:
        print("result", add(a, b))
    elif choice == 2:
        print("result", sub(a, b))
    elif choice == 3:
        print("result", mul(a, b))
    elif choice == 4:
        print("result", div(a, b))
    elif choice == 5:
        print("result", "quite")
        break

    else:
        print("invalid choice ,try again")






