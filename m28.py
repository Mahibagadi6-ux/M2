# FUNTIONS : funtionas are executes the block of code and it oganize data reduce the rechanbale
def greet():
    print("hello")
greet()

# funtion parameter
def fun(name,age):
    print(f"hello {name} you are {age} years old")
fun("mahesh",19)

# defualt parameter
def fun(name, age=19):
    print(f"hello {name} you are {age} years old")
fun("mahesh")

#local and global value
def grret(name,age):
    name = "mahesh"
    age = 19
    print(f"hello {name} you are {age} years old")
#print(name)# shows error due to that is the local variable
age = 10 # it does not  shows any error because of the brecuase it is the  global variable and it can assign to the in to the def funtion
print(age)

#returning value funtion
def funtion(num):
    for i in range(1,11):
        print(f"{num}x{i} = {num*i}")
funtion(100)
def funtion(num):
    for i in range(1,11):
        return f"{num}x{i} = {num*i}"
funtion(100)

def fun(num):
    return int(str(num)*3)
fun(10)

a = 100
c = a + fun(10)
print(c)


def greet():
    print("she said hi to me")
greet()

def user(name):
    print("hello " + name)
user("mahesh")

def fun(a,b):
    return a + b

fun(10,20)
d = 100
f = d + fun(10,20)
print(f)
