"""Dataclass version of the Python classes described in Python Object
Oriented Programming - For Beginners Youtube Video"""

from typing import List
from dataclasses import dataclass, field


@dataclass
class Student:
    __slots__ = ["name", "age", "grade"]
    name: str
    age: int
    grade: int

    def get_grade(self):
        return self.grade


@dataclass
class Course:
    name: str
    max_students: int
    students: List[int] = field(default_factory=list)

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print()
print(
    f"Hello, My name is {course.students[0].name}, I am {course.students[0].age} years old and I have grade of {course.students[0].grade}")
print(
    f"Hello, My name is {course.students[1].name}, I am {course.students[1].age} years old and I have grade of {course.students[1].grade}")
print(
    f"Hello, My name is {course.students[2].name}, I am {course.students[2].age} years old and I have grade of {course.students[2].grade}")
print(
    f"The average grade for the {course.name!r} course is {course.get_average_grade():.2f}")
