def combinations(base, power):
    list = []
    for i in range(2, base+1):
        for j in range(2, power+1):
            if pow(i,j) not in list:
                list.append(pow(i,j))
    return len(list)
print(combinations(100,100))
