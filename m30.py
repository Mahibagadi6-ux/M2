# recursion : it called repeat itself
# factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))

# sum of numbers using recursion
def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n-1)
print(sum_num(10))



mult = lambda a,b: a*b
print(mult(10,20))


def average(*nums):
    return (sum(nums))/len(nums)
print(average(1,2,3,4,5))



