# decorators are use to modify the code and funtion without changing actual code
def decorater_name(func):
    def wrapper():
        print("Namaskara")
        func()
        print("TAke care")
    return wrapper
@decorater_name
def intro():
    print("i am mahesh from yadagir")
intro()


def mahesh_name(surname):
    def wrapper():
        print("Mahesh")
        surname()
        print("From Yadagir")
    return wrapper
@mahesh_name
def surname_():
    print("Bagadi")
surname_()

@mahesh_name
def bye():
    print("byeeeeeeee")
bye()

def Sudden_met(fun):
    def wrapper():
        print("hi jassu how are you ")
        fun()
        print("i am  also fine")
    return wrapper
@Sudden_met
def mama():
    print("i am good mama , what about you ")
mama()


# Decorater with the argument
def show_result(func):
    def wrapper(a,b):
        print("result: ",end="")
        func(a,b)
    return wrapper
@show_result
def add(a,b):
    print(a+b)
@show_result
def sub(a,b):
    print(a-b)
@show_result
def mul(a,b):
    print(a*b)

add(1,2)
sub(3,4)
mul(5,6)

#logging
def logger(func):
    def wrapper(a,b):
        print(f"Funtion as  '{func.__name__}' been called .")
        func(a,b)
    return wrapper
@logger
def add(a,b):
    print(a+b)
@logger
def sub(a,b):
    print(a-b)
@logger
def mul(a,b):
    print(a*b)

add(1,2)
sub(3,4)
mul(3,4)










