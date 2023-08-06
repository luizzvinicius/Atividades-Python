def fatorial(n):
    fat = 1
    for i in range(2, n+1):
        fat *= i
    return fat


a = fatorial(0)
print(a)


def fibonacci(n):
    a = s = 0
    b = 1
    for i in range(n):
        s = a + b
        a = b
        b = s
        print(a, end=" ")


a = 2
b = 7
a = b - a
print(a)
