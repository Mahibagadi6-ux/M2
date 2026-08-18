square = lambda x:x**2
print(square(5))
  # fizz buzz play
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

# map funtion using
nums = [1,2,3,4,5,6,7,8,9]
double  = list(map(lambda x: x*2, nums))
print(double)

nums = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda x :  x % 2 == 0,nums))
print(evens)


duplicate = [1,2,3,4,5,5,6,7,7,9,9,10,10]
remove_duplicate = list(set(duplicate))
print(remove_duplicate)

def vowel_counter(s):
    return sum(1 for char in s.lower() if char in 'aeiou')
print(vowel_counter("hello world"))


# sind the  missing number
def find_missing_number(nums,n):
    return n * (n+1) // 2 -sum(nums)
print(find_missing_number([1,2,4,5],5))
# anagram checker
def anagram_checekr(s1,s2):
    return sorted(s1.lower()) == sorted(s2.lower())
print(anagram_checekr(" world","hello"))