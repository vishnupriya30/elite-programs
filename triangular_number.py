def triangular_number(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum + i
    return sum
def divisor(num):
    list = []
    for i in range(1, num+1):
        if num % i == 0:
            list.append(i)
    return len(list)
def requires_num(divisors):
    for i in range(6000,6010):
        if divisor(triangular_number(i)) > divisors:
            return triangular_number(i)
print(requires_num(500))
