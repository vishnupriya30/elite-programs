def fibonacci(n):
    list = []
    for i in range(1, n + 1):
        if i == 1:
           first = 1
           list.append(1)
        elif i == 2:
           second = 2
           list.append(2)
        else:
           current = first + second
           list.append(current)
           first = second
           second = current
    return list
def sum_of_even(n):
     sum = 0
     s = fibonacci(n)
     for i in range(0, len(s)):
         if s[i] % 2 == 0 and s[i] <= 4000000:
             sum = sum + s[i]
     return sum
    
print(sum_of_even(100))
