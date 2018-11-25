def prime(n):
    list = [2]
    for i in range(3,n,2):
        count = 0
        if i != 2 and i % 2 != 0:
            for j in range(2,int(i**(1/2)) + 1,1):
                if i % j == 0:
                    count = count + 1
            if count == 0 and len(list) < 10002:
               list.append(i)
    return list[10000]
print(prime(1000000))
