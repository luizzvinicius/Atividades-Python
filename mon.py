def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


a = fatorial(5)
# print(a)


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
