# map ,filters , reduce()
# This are the funtional programming tools in the python funtions to iterables , clean and concise way.
#1. map()
nums = [1,2,3,4,5,6,7,8,9]
result = []
for num in nums:
    result.append(num*2)
print(result)


nums = [1,2,3,4,5,6,7,8,9]
def double(x):
    return x*2
result = map(double, nums)
print(list(result))


nums = [1,2,3,4,5,6,7,8,9]
res = map(lambda x: x*2, nums)
print(list(res))


