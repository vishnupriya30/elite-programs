def sum_of_powers(num):
    sum = 0
    while num > 0:
        sum = sum + pow((num % 10), 5)
        num = num // 10
    return sum
def special_numbers(low, high):
    #list = []
    sum_of_numbers = 0
    for i in range(low, high + 1):
        if i == sum_of_powers(i):
            #list.append(i)
    #return list
            sum_of_numbers = sum_of_numbers + i
    return sum_of_numbers

print(special_numbers(2, 200000))
