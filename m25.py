NUM = [1,2,3,4,5,6,7,8,9]
count = 0
for num in NUM:
    count = count + num
print(count)


#dictionary comparsion
l = [1,2,3,4,5,6,7,8,9]
dl = []
for num in l:
    dl.append(num*2)
print(dl)


# looping through dictionary
student_marks = {"mahesh":85,"sachin":76,"vishwa":90}
for student in student_marks.items():
    print(student)
students = ["mahesh","sachin","vishwa"]
marks = [10,20,30]
student_marks = {}
for idex, student in enumerate(students):
    student_marks[student] = marks[idex]
print(student_marks)

name = "chandan"
for index, ketter in enumerate(name):
 print(ketter*(index))

students = ["mahesh","sachin","vishwa"]
marks = [10,20,30]
student_marks = {}
for i in range (len(students)):
    student_marks[students[i]] = marks[i]
print(student_marks)


l = [1,2,3,4,5,6,7,8,9]
dl = [n**2 for n in l]
print(dl)

l = [x for x in range (1,10)]
dl = [x*2 for x in l]
print(dl)

l = [x for x in range (1,10)]
dl = [i for i in l if i%2!=0]
print(dl)

l = [x for x in range (1,10)]
dl = [i for i in l if i%2==0]
print(dl)

l = ["mahesh","sachin","vishwa"]
dl = [x[1] for x in l ]
print(dl)

name = ["mahesh","sachin","vishwa"]
dl = {name:len(name) for name in name}
print(dl)


cp = {
    "bengaluri":20,
    "belagavi":10,
    "chittardurga":18
}
lc = {key:value for key, value in cp.items() if value>10}
print(lc)

x = input("enter the list of integers :  ").split()
dl = [int(num) for num in x]
print(dl)


name = ["mahesh","sachin","vishwa"]
dl = [len(name) for name in name]
print(dl)





