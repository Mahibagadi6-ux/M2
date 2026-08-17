from pydantic_core.core_schema import none_schema


def even_odd(n):
    if n%2==0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")
print(even_odd(7))
print(even_odd(5))


def max_num(a,b,c):
    if a>b and a>c:
        return "a is biggset"
    elif b>c and b>a:
        return "b is the biggset number"
    elif c>a and c>b:
        return "c is the biggset number"
    else:
        return "none"

print(max_num(90,50,20))


square = lambda x: x**2
print("square",square(10))
print("square",square(20))