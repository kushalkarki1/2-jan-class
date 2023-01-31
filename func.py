# def welcome():
#     print("Welcome everyone to function class")

# welcome()
# welcome()


# def welcome():
#     print("Welcome students!")

# welcome() # call for function execution
# welcome # call by reference


# def welcome(name, address): # parameters
#     print("Welcome", name)
#     print("Address:", address)

# name = input("Enter your name: ")
# address = input("Enter your address: ")
# welcome(name, address) # arguments

# a = 10
# b = 20
# total = a + b
# print("The sum of {} and {} is {}".format(a, b, total))
# print(f"The sum of {a} and {b} is {total}.")


# def profile(name, address, contact):
#     print(f"Name: {name}")
#     print(f"Address: {address}")
#     print(f"Contact: {contact}")

# profile("Ram", "Ktm", "987654321") # positional arguments
# profile("Ram", "987654321", "Ktm")
# profile(contact="87654", name="Hari", address="Ktm") # keyword arguments


# def addition(num1, num2=1):
#     print(num1+num2)

# addition(10, 5)


# def addition(num1, num2):
#     print(num1 + num2)

# def product(num1, num2):
#     return num1 * num2


# a = addition(10, 20)
# print(f"Addition: {a}")
# res = product(10, 5)
# print(f"Product: {res}")


def multiple_arguments(*a):
    print(a)

multiple_arguments(1, 2, 3, 4, 5, 6, 7, 8, "python", "Ram")


def multiple_keyword_arguments(**k):
    print(k)


multiple_keyword_arguments(name="Ram", contact="876543", address="9876543", _id=87)
