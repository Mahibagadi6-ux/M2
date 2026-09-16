# # hw given by the chandan anna
# def loggegr(fun):
#     def wrapper(a,b):
#         print(f"funtion '{fun.__name__}' has been calling")
#         fun(a,b)
#     return wrapper
# @loggegr
# def add(a,b):
#     print(a+b)
# @loggegr
# def subtract(a,b):
#     print(a-b)
# @loggegr
# def multiply(a,b):
#     print(a*b)
# add(1,2)
# subtract(2,3)
# multiply(3,4)
#
#
# import time
# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print("Time taken :",end - start,"seconds")
#     return wrapper
# @timer
# def long_task():
#     print("Task starteded")
#     time.sleep(3)
#     print("Task ended")
# long_task()


def border(func):
    def wrapper():
        print("===")
        func()
        print("===")
    return wrapper
def arrow(func):
    def wrapper():
        print(">>>",end="")
        func()
    return wrapper

@border
@arrow
def my_name():
    print("Mahesh")
my_name()

def allow_only(Allowed_name):
    def decorater(func):
        def wrapper(name):
            if name == Allowed_name:
                func(name)
            else:
                print("Allowed name not allowed")
        return wrapper
    return decorater
@allow_only("Mahesh")
def view_data(name):
    print(name)
    print("Here your data")
view_data("Mahesh")
view_data("Mahesh_b")




