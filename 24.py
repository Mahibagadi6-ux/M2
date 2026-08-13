for i in range(1,31):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}",end=" ")
        print()

total = 0
for i in range(1,10):
    total = total + i
print(total)

name = "mahesh"
count = 0
for name in name:
    if name in "aeiou":
        count = count + 1
print(count)




