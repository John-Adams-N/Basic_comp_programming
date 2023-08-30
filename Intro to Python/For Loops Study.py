
for x in range(5):
    print(x, end=" ")
    

product = 1
for n in range(1, 10):
    product = product * n
print(product)


def to_celcius(x):
    return( x-32)*5/9
for x in range (0,101,10):
    print(x, to_celcius(x))


for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()


# Recursion TODO

def factorial(n):
    print("Factorial called with" + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    return n * factorial(n-1)
    print("Returning" + str(result) + " for factorial of" + str(n))
factorial(4)

# 2 TODO

# The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1.
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15
# Fill in the gaps to make this work

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# 3 TODO

def is_power_of(number, base):
    # Base case: when number is smaller than base.
    # If number is equal to 1, it's a power (base**0).
    if number % base == 0:
        if number < base:
            if number == 1:
                return number < base

    else:
        # Recursive case: keep dividing number by base.
        return is_power_of((number - 1) / base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False

