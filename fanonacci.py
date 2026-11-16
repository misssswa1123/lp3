# non recursive
def fib_iterative(n):
    if n <= 1:
        print(n, end=' ')
    a, b = 0, 1
    print(a, b, end=' ')
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
        print(b, end=' ')


n = int(input("Enter n: "))
fib_iterative(n)
#recursive

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter number of terms: "))

print("Fibonacci series:")
for i in range(n):
    print(fib(i), end=" ")