# num = int(input("Enter any number: "))

# if num > 0:
#     print("The number is positive.")
# else:
#     print("The number is negative.")

# user input, int
# print either that number is odd or even

# num = int(input("Enter any number: "))
# rem = num % 2
# if rem == 0:
#     print("The number is even")
#     print("The number was", num)
# else:
#     print("The number is odd")


num = int(input("Enter any number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero.")

# take user input
# print "exactly divided by 3" if exactly divisible by 3
# print "exactly divided by 5" if exactly divisible by 5
# print "exactly divided by 7" if exactly divisible by 7

num = int(input("Enter any number: "))
if num % 3 == 0:
    print("Exactly divided by 3")

if num % 5 == 0:
    print("Exactly divided by 5")

if num % 7 == 0:
    print("Exactly divided by 7")