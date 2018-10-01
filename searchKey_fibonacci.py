def fibonacci(upperbound):
    list = [0, 1]
    first = 0
    second = 1
    for i in range(2, upperbound + 1):
        current = first + second
        list.append(current)
        first = second
        second = current
    return list
def search(key, upperbound):
    list = fibonacci(upperbound)
    if key in list:
        return "IsFibo"
    else:
        return "IsNotFibo"
print(search(51, 100))
