#home work
i = 1
while i<=10:
    print(i)
    i=i+1

i = 1
while i <= 20:
    print(i)
    i = i + 2

sets = 8
while sets  > 0:
    print("sets are avilable ",sets)
    booking = input("do you have seats yes or no? : ")
    if booking == "yes":
        sets = sets - 1
        print("seat booked successfully")
    else:
        print("seat  are not avilable ")
        break
if sets == 0:
    print("sets are fulled  sorry ")


n = 10
while n>1:
    print(n)
    n = n-1
else:
    print(" happy new year")
