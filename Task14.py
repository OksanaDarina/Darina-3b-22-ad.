class Student:
 def __init__(self, name, surname, age, speciality):
  self.name = name
  self.surname = surname
  self.age = age
  self.speciality = speciality

 def info(self):
  print(f"{self.name}-{self.surname}, {self.age} лет, {self.speciality}")
classmate = Student("Екатерина", "Шульман", 44, "Политолог")
classmate.info()