from PTS import *
from Department import Department
import datetime
import random
class Diary:
    def __init__(self):
        self.grades = {}
        self.absences = {}

    def writegrade(self,teacher,student,subject,grade):
        try:
            teacher.checksubject(subject)
            self.grades[(student.name,teacher.subject)]=grade
        except Exception as e:
            print(e)
    def writeabsence(self,student,year,month,day):
        date = datetime.datetime(year, month, day)
        date = date.strftime("%d" + "/" + "%m" + "/" + "%Y")
        student.absence[("5",date)]=False
    def writegrades(self,students,teachers):
        file = open("grades.txt", "w")
        for i in range(1, 6):
            date = datetime.datetime(2020, 6, i)
            dateS = date.strftime("%d" + "/" + "%m" + "/" + "%Y")
            date = date.strftime("%d" + "/" + "%m" + "/" + "%Y" + "   " + "%H" + ":" + "%M")
            grades = []
            for x in students:
                teacher = teachers[random.randint(0, 4)]
                grade = random.randint(1, 5)
                grades.append(grade)
                try:
                    x.checkabsence(dateS)
                    file.write(f"Grade {grade} given {date} subject {teacher.subject}" + "\n")
                    self.writegrade(teacher, x, teacher.subject, grade)
                    x.grades[(teacher.subject,date)]=grade
                    grades.append(grade)
                except Exception as e:
                    print(e)
        file.close()
        self.average(students,grades)
    def average(self,students,grades):
        pass



