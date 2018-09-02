def fibo(n):

    if n == 0:
        return 0
    elif n < 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(10))