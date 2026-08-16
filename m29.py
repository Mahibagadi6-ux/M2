# advanced in funtion
# variable length arguments: we want specify without error while us ethis method
def fun(*a):
    print(a)
fun(2,3,4,56)


def fun(*nums):
    return sum(nums)
print(fun(1,2,3,4,5))
# its apl]plies tuples only


def fun(**nums):
    for key, value in nums.items():
        print(key, value)
fun(name="mahesh",age = 20,favorite_color = "red")
# its appily the dictionary


# lamda funtiona are very imp bcz its makes uniqe code  bigger one into smalller
add = lambda a,b: a+b
print(add(10,20))

mult = lambda a,b: a*b
print(mult(10,20))


double = lambda a : 3*a
print(double(10))

students = [
    {
        "name" : "mahesh",
        "age" : 18,
        "favorite_color" : "red"
    },
    {
        "name" : "vishwanath",
        "age" : 23,
        "favorite_color" : "green"
    },
    {
        "name" : "jasvik",
        "age" : 20,
        "favorite_color" : "blue"



    }

]
students.sort(key=lambda x:x["age"],reverse=True)
print(students)

# name sort list
students = [
    {
        "name" : "mahesh",
        "age" : 18,
        "favorite_color" : "red"
    },
    {
        "name" : "vishwanath",
        "age" : 23,
        "favorite_color" : "green"
    },
    {
        "name" : "jasvik",
        "age" : 20,
        "favorite_color" : "blue"



    }

]
students.sort(key=lambda x:x["name"])
print(students)


def sort_name(names):
    return sorted(names,key=lambda name:name)
print(sort_name(["mahesh","ravi","chetan","arpitha","anil"]))

# nested function
def details(a,b):
    def add():
        return a+b
    def mult():
        return a*b
    def sub():
        return a-b
    print(add())
    print(mult())
    print(sub())
details(12,23)

