num = 0
while num <= 10:
    num = num + 1
    print(num)

num = 1
while num <= 10:
    i = 1
    while i<=1:
        if num%2==0:
            print(num)
        i = i + 1
    num = num + 1

num = 0
while num <= 10:
    i = 1
    while i<=1:
        if num%2 != 0:
            print(num)
        i = i + 1
    num = num + 1

num = 0
while num <= 10:
    if num==5:
        break
    print(num)
    num = num + 1

num = 0
while num <= 10:
    num = num + 1
    if num==5:
        continue
    print(num)


i = 0
while i <= 10:
    j = 0
    while j <= i:
        print("*", end=' ')
        j = j + 1
    print()
    i = i + 1


i = 0
while i <= 10:
    j = 0
    while j <= 5:
        print("*", end=' ')
        j = j + 1
    print()
    i = i + 1

i = 5
while i >= 1:
    j = 0
    while j <= i:
        print("*", end=' ')
        j = j + 1
    print()
    i = i - 1


i = 1
while i <= 10:
    j = 0
    while j <= 10:
        print(f"{i} X {j} = {i*j}", end='  ')
        j = j + 1
    print()
    i = i + 1

i = 1
while i <= 100:
    j = 1
    while j <= 10:
        print(i, end=' ')
        i = i + 1
        j = j + 1
    print()


# factor program
i = 1
while i <= 100:
    j = 1
    print("factor number:", i, end=" ")

    while j <= i:
        if i % j == 0:

            print(j, end=" ")
        j = j + 1
    print()
    i = i + 1

i = 2
while i <= 100:
    j = 2
    prime = True
    while j < i:
        if i%j == 0:
            prime = False
            break
        j = j + 1
    if prime:
        print(j, end=" ")
    i = i+1


