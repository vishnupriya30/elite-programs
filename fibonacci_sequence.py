def fib(num):
      if num == 1 or num == 2:
          return 1
      else:
          return fib(num-1)+fib(num -2)
def no_of_digits(num):
      num = str(num)
      return len(num)
def required_num(digit):
      for i in range(1, 50):
           if no_of_digits(fib(i)) == digit:
               return i
print(required_num(5))
