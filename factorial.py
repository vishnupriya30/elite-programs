import math
def factorial(num):
    return math.factorial(num)
def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum = sum + (num % 10)
        num = num // 10
    return sum
print(sum_of_digits(factorial(100)))
