from abc import ABC,abstractmethod
import uuid

class Person(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    @abstractmethod
    def introduce(self):
        pass



class Teacher(Person):
    def __init__(self,name,surname,subject):
        super().__init__(name,surname)
        self.subject = subject
    def introduce(self):
        print(f"Hello, my name is {self.name}, and i am teacher!")
    def checksubject(self,subject):
        if self.subject != subject:
            raise Exception("WrongSubject")


class Student(Person):
    def __init__(self,name,surname,address,Class):
        super().__init__(name,surname)
        self.id = uuid.uuid4()
        self.address = address
        self.Class = Class
        self.grades = {}
        self.absence = {}
    def introduce(self):
        print(f"Hello, my surname is {self.surname}, and i am student!")

    def checkabsence(self,date):
        if ("5",date) in self.absence:
            raise Exception("Absence")


