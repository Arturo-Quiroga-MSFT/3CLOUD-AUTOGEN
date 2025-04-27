# filename: fibonacci_14.py

def fibonacci(n):
    # Function to calculate the nth Fibonacci number
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Calculate the 14th Fibonacci number
fibonacci_14 = fibonacci(14)
print(f"The 14th Fibonacci number is: {fibonacci_14}")
