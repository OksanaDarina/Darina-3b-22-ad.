class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age

 def information(self):
  print(f"Имя: {self.name}, возраст: {self.age}")
person = Person("Виктория", 13)
person.information()