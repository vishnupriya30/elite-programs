def isPalindrome(n):
    rev = 0
    n1 = n 
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    if n1 == rev:
        return True
    else:
        return False
def product():
    list = []
    for i in range(100, 1000):
         for j in range(100, 1000):
            s = i * j
            if(isPalindrome(s)):
                list.append(s)
    return list
print(product())
