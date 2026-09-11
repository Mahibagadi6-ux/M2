
try:
    file = open("family.massage txt","w")
    file.read("\n mallikajun \n malappa \n pacchi")
except Exception as e:
    print(f"error found {e}")
else:
    print("error bandilla  well done you wrote current code ")
finally:
    print("file closed")
    file.close()
students = ["mahesh","vishwa","vidya","jassu","indramma","sulappa"]
file = open("family.txt","w")
for students in students:
    file.write(f"{students}\n")
file.close()

students = ["mahesh","vishwa","vidya","jassu","indramma","sulappa"]
with open("family.trt","w") as file:
    for student in students:
        file.write(f"{student}\n")
file.close()