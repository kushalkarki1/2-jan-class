# for(i=0;i<10;i++){

# }

# for <variable> in <iterable_object>:
    # code for execution

# a = [10, 20, 30, 40, 50, 60]

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])

# for i in a:
#     print(i)


# for i in range(100):
#     print(i)

# range(start, stop, step)
# range(10) => start=0, stop=9, step=1
# range(1, 10) => start=1, stop=9, step=1
# range(1, 10, 2) => start=1, stop=9, step=2

# total = 0
# for i in range(1, 11):
#     total = total + i

# print(total)

# total = sum(range(1, 11))
# print(total)

# total = 0
# for i in range(2, 21, 2):
#     total = total + i

# print(total)

# take 5 input of student name
# append them in a list and print
# make sure, first letter of every name is capitalized


# students = []
# for i in range(5):
#     name = input("Enter your name: ")
#     students.append(name.capitalize())

# print(students)


# while <condition>:
    # code to execute

# while True:
#     print("hello students!")

# a = 0

# while a < 5:
#     print("I am ", a)
#     a = a + 1

# a = 1
# while a < 20:
#     if a % 2 == 0:
#         print(a)
#     a = a + 1

# a = 2
# while a < 20:
#     print(a)
#     a = a+2

# total = 0
# a = 2
# while a < 20:
#     total = total + a
#     a = a+2

# print(total)


# a = "19d89d43d56"
# b = a.split("d")
# total = 0
# for i in b:
#     total = total + int(i)

# print(total)

# username = "abc@gmail.com"
# password = 12345
# take user input until match
# username = input("Enter username: ")
# password = input("Enter password: ")
# while username != "abc@gmail.com" or password != "12345":
#     username = input("Enter username: ")
#     password = input("Enter password: ")
# print("Success")


# break, continue

# for i in range(1, 10):
#     print(i)
#     if i % 7 == 0:
#         break


# while True:
#     a = int(input("Enter number: "))
#     if a == 100:
#         break

# for i in range(1, 10):
#     if i % 7 == 0:
#         continue
#     print(i)

while True:
    a = int(input("Roll your dice: "))
    if a == 1 or a == 6:
        continue
    else:
        break