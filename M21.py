is_failed = True
while is_failed:
    print('try agian')
i = 0
while i<1000:
    print(i)
    i+=1
    if i>100:
        break
 # even number
num = 1
while num<=10:
    i=1
    while i<=1:
        if num % 2==0:
            print(num,"even")
        else:
            print(num,"odd")

        i+=1
    num+=1

# square pattern
i = 1
while i<=5:
    j=1
    while j<=5:
        print("*" ,end = " ")
        j+=1
    print()
    i= i+1


# right angle triangle
i=1
while i<=5:
    j=1
    while j<=i:
        print("*" ,end = " ")
        j+=1
    print()
    i= i+1

# number triangle
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end = " ")
        j+=1
    print()
    i= i+1


# repeted number triangle
i = 1
while i<=5:
    j=1
    while j<=i:
        print(i,end = " ")
        j+=1
    print()
    i= i+1


# inverted triangle
i=5
while i>=1:
    j=1
    while j<=i:
        print("*" ,end = " ")
        j+=1
    print()
    i=i-1

# mutiplication table
i=1
while i<=3:
    j=1
    while j<=10:
        print(i,"x",j,"=",i*j)
        j+=1
    print()
    i=i+1


# factor number
i = 1
while i<=10:
    j = 1
    print("factor of",i,"=",end="" )
    while j<=i:
        if i%j==0:
            print(j,end=" ")
        j+=1
    print()
    i=i+1


# prime number
num = 2
while num<=20:
    i = 2
    prime = True
    while i<num:
        if num%i==0:
            prime = False
            break
        i+=1
    if prime:
        print(num,end=" ")
    num+=1


# 100 elements in one row
i = 1
while i<=100:
    j = 1
    while j<=10:
        print(i,end = " ")
        i=i+1
        j=j+1



