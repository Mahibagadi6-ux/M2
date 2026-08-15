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