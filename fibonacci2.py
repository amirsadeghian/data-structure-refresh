def fib2(n):
    if n in {0,1}:
        return n
    else:
        previous =  0
        fib_number = 1
        for _ in range(2,n+1):
            previous, fib_number = fib_number , previous + fib_number
        return fib_number
result = fib2(4)
print(result)