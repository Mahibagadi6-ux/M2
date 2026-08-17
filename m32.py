"""Given an integer,n, perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of   6 20 to , print Weird
If  is even and greater than  20 , print Not Weird
Input Format"""

n = int(input("Enter an integer: "))
if n % 2 != 0:
    print("Weird")
else:
    if 2 >= n >= 5:
        print("Not Weird")
    elif 6 >= n >=20:
        print("Weird")
    else:
        print("Not Weird")



# leap year
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = False

        if year % 100 == 0:
            leap = True

    # Write your logic here

    return leap


year = int(input())