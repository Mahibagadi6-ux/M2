# even or odd
"""num = int(input())
print("even" if num %2 == 0 else "odd")

# reverse string
s  = "python"
print(s[::-1])

# fabonacci series
n = int(input("enter an number  :  "))
a , b  = 0,1
for i in range(n):
    print(a, end = " ")
    a, b = b, a+b

# palindrome checker
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]
print(is_palindrome("python"))


# check leap year
year = int(input("enter the year :  "))
if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print("leap year ")
else:
    print("not a leap year")

#list compransion challenge generate the  sqauar using for loop
x = [x**2 for x in range(1,101)]
print(x)"""

# checking arm strong nume armstrong number
"""for digit in num_str: Loops through each character (digit) in 
the string version of the number (num_str).int(digit): Converts 
the character back into a whole number (integer) so math can be
done on it.** power: Raises that individual digit to the power of power 
(which is the total count of digits in the original number).sum(...): 
Adds up all of those powered values into a single total sum.num == ...:
Compares this final calculated sum against the original number (num)."""
def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    return num == sum(int(digit) ** power for digit in num_str)
print(is_armstrong(153))




