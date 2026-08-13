# for loop
name = "mahesh"
for name in name:
    print(name)



name = "mahesh"
for name in name:
    print(name*6)


# we want leran about thwe enumarate and index
fruits = ["apple", "banana", "cherry"]
for index,fruit in enumerate(fruits):
    print(index,fruit)


name = "mahesh"
for index,name in enumerate(name):
    print(name*(index+1))


cities = ["bengaluru","dhavangere","chittardurga","chikkaballapur"]
for city in cities:
    if city== "chittardurga":
        print(city,"i found")
        break
    print(city)

cities = ["bengaluru", "dhavangere", "chittardurga", "chikkaballapur"]
for city in cities:
    if city == "chittardurga":
        print(city,"i not found")
        continue
    print(city)

laddus = 5
friends = ["mahesh","mallikarjun","mudukappa","malappa"]
for friend in friends:
    if laddus > 0:
        print(friend,'took one laddu')
        laddus = laddus - 1
    else:
        print("no more left laddus ")

for i in range(6):
    for j in range(6):
        print(f"[{i}x{j}= ({i*j})]")
    print()

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
        j = j + 1
    print()

for i in range(1, 6):
    for j in range(1,6):
        print("*", end=" ")
        j = j + 1
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")

    print()


for i in range(6):
    for j in range(1,4):
        print(j,end=" ")

    print()


for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()




