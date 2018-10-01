#function returns binary representation of a number
def binary(num):
    return int(bin(num)[2:])
def reverse(num):
    n = str(num)
    return n[::-1]
 #function returns true if num , its reverse is same and  binary of num, its reverse is same
def is_palindrome(num):
    if num == int(reverse(num)) and binary(num) == int(reverse(binary(num))):
        return True
    else:
        return False
#function returns sum of all double base palindromes till upperbound
def sum_of_all(upperbound):
    sum = 0
    for num in range(1,upperbound):
       if is_palindrome(num):
           sum = sum + num
    return sum
print(sum_of_all(1000000))
