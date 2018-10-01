#function to return whether number is prime or not
def is_prime(num):
     flag  = 0
     for i in range(2, int(num ** (1/2)) + 1):
         if num % i == 0:
             flag = 1
             return False
     if flag == 0:
          return True
#circular_nums is a list of circular numbers of a given number and this function returns true if all the numbers in list are prime
def is_circular_prime(num):
     circular_nums = []
     n = str(num)
     count = 0
     for i in range(1, len(n) + 1):
         n = n[1:] + n[0]
         circular_nums.append(n)
     for i in range(0, len(n)):
         if is_prime(int(circular_nums[i])) == True:
             count = count + 1
     if count == len(circular_nums):
         return True
     else:
         return False
 #circular_primes is a list of all circular prime numbers till upperbound and then returns length of list
def circular_prime(upperbound):
     circular_primes = []
     for num in range(2, upperbound):
         if is_circular_prime(num) == True:
              circular_primes.append(num)
     return len(circular_primes)
print(circular_prime(1000000))
