def sum_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i ** 2
    return sum
def square_of_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum ** 2
print(square_of_sum(100) - sum_of_squares(100))
