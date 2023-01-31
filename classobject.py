# Object Oriented Programming
# Class and Object
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

# class Projector:
#     # Initializer function
#     def __init__(self, color, year, model="NEC"):
#         self.color = color
#         self.year = year
#         self.model = model

#     def visualise(self):
#         print(f"Projector of model {self.model} is visualising")

#     def description(self):
#         print(f"Color: {self.color}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")

#     def __str__(self):
#         return self.model

#     def __repr__(self):
#         return f"{self.model} - {self.year}"

# p1 = Projector("White", 2022, "NEC")
# p2 = Projector("Red", 2021, "Acer")
# # p1.visualise()
# # p2.visualise()
# # p2.description()
# # print(p1.__dict__)

# projectors = []
# for i in range(2):
#     color = input("Enter color: ")
#     year = input("Enter year: ")
#     model = input("Enter model: ")
#     p = Projector(color, year, model)
#     projectors.append(p)

# print(projectors)


# class Student:

#     def __init__(self, _id, name, contact, address):
#         self._id = _id
#         self.name = name
#         self.contact = contact
#         self.address = address
#         self.total_attendance = 0

#     def update_attendance(self):
#         self.total_attendance += 1

#     def view_attendance(self):
#         return self.total_attendance

# s = Student(1, "Ram", "87654", "Ktm")
# s2 = Student(2, "Shyam", "8765", "Bkt")
# s.update_attendance()
# s2.update_attendance()
# s2.update_attendance()
# print(s.view_attendance()) # 1
# print(s2.view_attendance()) # 2
# # print(Student.view_attendance(s))


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if price > 0:
#             self.__price = price


# tshirt = Product("Tshirt", 500)
# jacket = Product("Jacket", 1000)
# print(f"Before setting: {tshirt.price}")
# tshirt.price = -1
# print(f"After setting: {tshirt.price}")


# class Calculator:
#     def __init__(self, num1, num2):
#         self.a = num1
#         self.b = num2

#     def add(self):
#         return self.a + self.b

#     def difference(self):
#         return self.a - self.b

#     def product(self):
#         return self.a * self.b

#     def division(self):
#         return self.a / self.b

#     @staticmethod
#     def square_root(num):
#         return num**0.5


# c = Calculator(10, 20)
# print(c.add())
# print(Calculator.square_root(25))


# class Student:
#     college = "ABC College" # class or static variable

#     def __init__(self, name, contact):
#         self.name = name
#         self.contact = contact

# print(Student.college)
# s = Student("Ram", "657654")
# print(s.college)
# print(s.__dict__)


# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     @classmethod
#     def create_user_with_random_password(cls, username):
#         return cls(username, "Default_password")

# u = User("ram@gmail.com", "Demo12345")
# print(u.__dict__)

# u2 = User.create_user_with_random_password("hari@gmail.com")
# print(u2.__dict__)