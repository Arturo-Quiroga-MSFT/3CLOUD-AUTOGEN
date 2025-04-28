# filename: fibonacci_14.py

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

# Calculate the 14th Fibonacci number
fib_14 = fibonacci(14)
print("The 14th Fibonacci number is:", fib_14)
