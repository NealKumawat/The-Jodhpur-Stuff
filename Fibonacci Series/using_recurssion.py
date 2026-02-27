def fib(n):
    fib(n) = fib(n-2) + fib(n-3)
    l.append(l[n-1])

l=[0, 1]
n=int(input("Give a number till you want the Fibonacci: "))
fib(n)