from PTS import *
from Department import Department
from Diary import Diary
import random
import datetime

def createstudents():
    students = []
    for i in range(1, 41):
        if i <= 20:
            student = Student(f"sn{i}", f"ss{i}", f"t{i}s{i}n{i}", 5)
        else:
            student = Student(f"sn{i}", f"ss{i}", f"t{i}s{i}n{i}", 6)
        students.append(student)
    return students

def createteachers():
    teachers = []
    for i in range(1,6):
        teacher = Teacher(f"tn{i}",f"ts{i}",f"Subject{i}")
        teachers.append(teacher)
    return teachers


if __name__ == '__main__':
    teachers = createteachers()
    students = createstudents()
    d5 = Department(5,teachers[0])
    d6 = Department(6,teachers[1])
    d5.get_students(students)
    d6.get_students(students)
    diary = Diary()
    diary.writegrades(students,teachers)
    diary.writeabsence(students[0],2020,6,4)



