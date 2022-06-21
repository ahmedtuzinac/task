class Department:
    def __init__(self,Class,teacher):
        self.Class = Class
        self.teacher = teacher
        self.students = []

    def get_students(self,students):
        self.students = list(filter(lambda x: x.Class==self.Class,students))

    def checkteacher(self,teacher):
        if teacher != self.teacher:
            raise Exception("WrongTeacher")


