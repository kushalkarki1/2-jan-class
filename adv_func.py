def greet():
    print("Hello Students!")
    print("Welcome everyone!")

g = greet # a = 10
g() # greet()


def addition(num1, num2):
    print(num1 + num2)

a = addition
a(10, 15)
# a = 5

def outer():
    def inner():
        print("I am inner function")
    inner()


outer()
# print(a)

def calculator():
    def addition(num1, num2):
        print(num1 + num2)
    return addition

add = calculator()
add(15 ,20)


def calculator(operator):
    def addition(a, b):
        return a + b
    def difference(a, b):
        return a - b
    def product(a, b):
        return a * b
    if operator == "+":
        return addition
    elif operator == "-":
        return difference
    elif operator == "*":
        return product

a = calculator("*")
print(a(20, 10))

# closure
def increment(num):
    def factor(val):
        return num + val
    return factor

increase_by = increment(20)
print(increase_by(10))
print(increase_by(30))


def welcome(name):
    print(f"Welcome {name}")

def bye_bye(name):
    print(f"Bye bye {name}")

def greet(func):
    func("Ram")

greet(bye_bye)


def decorate_function(func):
    def wrapper():
        print("Hello everyone!")
        func()
        print("Bye everyone!")
    return wrapper

@decorate_function
def welcome():
    print(f"Welcome everyone!")

w = decorate_function(welcome)
w()
welcome()

def smart_division(func):
    def wrapper(a, b):
        if b == 0:
            return "could not divide by zero"
        else:
            return func(a, b)
    return wrapper

@smart_division
def division(a, b):
    return a / b

# print(division)
# print(division(20, 10))
# print(division(20, 0))

import time

# start_time = time.time()
# total = 0
# for i in range(1, 100000001):
#     total += i

# print(total)
# print(time.time() - start_time)

def execution_time(fn):
    def wrapper(*a, **k):
        start_time = time.time()
        fn(*a, **k)
        print(time.time() - start_time)
    return wrapper

@execution_time
def example():
    print("Hello everyone")

@execution_time
def example2(n):
    print(f"{n} times")

@execution_time
def example3(x, y):
    print(x + y)

example()
example2(10)
example3(y=10, x = 20)