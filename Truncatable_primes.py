def is_prime(num):
    flag = 0
    if num == 1:
        return False
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            flag = 1
            return False
    if flag == 0:
        return True
#here list is a list of truncatable numbers of a given number and the returns tree if all numbers in list are prime
def is_truncatble_prime(num):
    n = str(num)
    list = []
    for i in range(0, len(n)):
        list.append(n[i:])
        list.append(n[:-i])
    list.remove('')
    for j in range(0, len(list)):
        if is_prime(int(list[j])) == False:
            return False
    return True
#returns sum of all truncatable primes till upperbound
def sum(upperbound):
    list = []
    sum =  0
    for i in range(22, upperbound + 1):
        if is_truncatble_prime(i) and len(list) != 11:
            list.append(i)
            sum = sum + i
    return sum
print(sum(1000000))

    
