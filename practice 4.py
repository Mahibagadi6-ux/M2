l = [num**2 for num in range(1,10)]
print(l)


d = [
    {
        "name" : "mahesh",
        "age" : 22
},
    {

        "name" : "vishwa",
        "age" : 20,
    },


]
for student in d:
    print(student["name"],"_",student["age"])



c = {
    "bangaluru": 90,
    "chittardurga":95,
    "davanagere":80,
    "honnavara":30
}
lc = {key:value for key, value in c.items() if value>90}
print(lc)
num = input("Enter a number: ").split()
l = [int(num)for num in num]
print(l)
rows =int(input("Enter number of rows: "))
matrix = []
for row in range(rows):
    row = [int(num) for num in input(f"enter row {row+1}").split()]
    matrix.append(row)
print(matrix)
