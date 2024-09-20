def fib(n):
     i = 1
     j = 1
     if n >= 3:
         for item in range(2, n):
             a = i + j
             i = j
             j = a
     yield j
