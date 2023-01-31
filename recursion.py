# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 => base condition

# 5! = 5 X (5-1)!

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(5))

def exponent(base, power):
    # base=5, power=3 => 125
    # base=2, power=4 => 16
    if power == 0:
        return 1
    return base * exponent(base, power-1)

print(exponent(5, 2)) # => 25
print(exponent(7, 3)) # => 343

# 2**4 => 2 X (2**3)