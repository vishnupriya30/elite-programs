def divisors(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    return sum
def amicable_pairs(upperbound):
    list = []
    for i in range(10, upperbound):
        for j in range(i, upperbound):
          if divisors(i) == j and divisors(j) == i:
                list.append(i)
                list.append(j)
    return list
print(amicable_pairs(300))
    
