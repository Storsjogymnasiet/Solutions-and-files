import random
import math

class Student:
    def __init__(self, name, year, acronym):
        self.name = name
        self.year = year
        self.acronym = acronym
        self.grade = None
        self.get_random_grade()
    
    def get_random_grade(self):
        self.grade = random.choice(["X", "Y", "Z"])

    def advance_year(self):
        self.year += 1

class Teacher:
    def __init__(self, name, age, wage, aura):
        self.name = name
        self.age = age
        self.wage = wage
        self.aura = aura
    
    def calculate_wage(self):
        self.wage = self.aura
    
    def compare_aura(self, other_teacher):
        if self.aura > other_teacher.aura:
            print(f"{self.name} har mer aura")
        else:
            print(f"{other_teacher.name} har mer aura")


student1 = Student("Rasmus Netler", 1, "rane1209")
student2 = Student("Wille Salmonsson", 1, "wisa1007")

teacher1 = Teacher("Mattias Leijon", 54, 10, 9001)
teacher2 = Teacher("Bill Burman", 30, 99999, math.inf)

print(student2.acronym)
print(student1.grade)
student1.grade = "Y"
print(student1.grade)

print(student2.year)
student2.advance_year()
print(student2.year)

print(teacher1.wage)
teacher1.calculate_wage()
print(teacher1.wage)

teacher1.compare_aura(teacher2)
