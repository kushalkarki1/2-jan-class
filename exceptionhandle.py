# try:
#     # block of code
# except Exception:
#     # block of code
# except ValueError:
#     # block of code
# except TypeError:
#     # block of code
# else:
#     # block of code
# finally:
#     # block of code

try:
    a = int(input("Enter any number: "))
    b = int(input("Enter another number: "))
except ValueError:
    print("can not convert to integer.")
else:
    print(f"Sum of {a} and {b} is {(a+b)}.")


name = input("Enter your name: ")
print(f"Name: {name}")