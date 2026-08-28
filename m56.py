
class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.__marks = {}
    def getmarks(self):
        return self.__marks
    def addmarks(self,subject,marks):
        self.__marks[subject] = marks
    def calculate_avgmarks(self):
        total = 0
        for subject in self.__marks:
            total += self.__marks[subject]
            avg = total/len(self.__marks)
            return avg
    def is_passed(self):
         has_failed = all(marks>35 for marks in self.__marks.values())
         if has_failed:
             print("is passed")
         else:
             print("is failed")
    def calculate_grade(self):
        percentage = self.calculate_avgmarks()  * 100
        if percentage >= 90:
            print("A")
        elif percentage >= 80:
            print("B")
        elif percentage >= 70:
            print("C")
        else:
            print("failed")
class reportcard:
    @staticmethod
    def __init__(student:student):
        student_marks = student.getmarks()
        print(f"{student.name}")
        print(f"{student.roll}")
        print("===== marks =====")
        for subject, marks in student_marks.items():
            print(f"{subject}: {marks}")
        print("====== student marks =====")
        print("=========== grade ======= =====")
        student.calculate_grade()
        print("===== avg marks =====")
        print(f"average: {student.calculate_avgmarks()}")

        print("===== passed  or not ======")
        student.is_passed()

a  = student(name="mahesh",roll=90)
b = student(name="vishwa",roll=80)
a.addmarks("match",100)
a.addmarks("science",90)
report = reportcard(a)

