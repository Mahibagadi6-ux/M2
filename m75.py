def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def dispalu_menu():
    print("SIMPLE CALCULATER")
    print("1.add \n 2.sub \n 3.mul \n 4.div \n 5.quite ")
while True:
    dispalu_menu()
    choice = int(input("Enter your choice: "))
    if choice in {1,2,3,4,5}:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
    if choice == 1 :
        print("Result:", add(a,b))
    elif choice == 2 :
        print("Result:", sub(a, b))
    elif choice == 3 :
        print("Result:", mul(a, b))
    elif choice == 4 :
        print("Result:", div(a, b))
    elif choice == 5 :
        print("quite")
        break
    else:
        print("Invalid choice! ,try again ")





