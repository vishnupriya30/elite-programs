def prime(n):
    sum = 0
    for i in range(3,n,2):
        count = 0
        if i % 2 != 0:
            for j in range(2,int(i**(1/2)) + 1):
                if i % j == 0:
                    count = count + 1
            if count == 0 and i <= 2000000:
                sum = sum + i
    return sum+2
print(prime(10))
    
