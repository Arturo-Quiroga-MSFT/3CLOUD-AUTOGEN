# filename: calculate_fibonacci.py
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    if n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Calculate the 14th Fibonacci number
nth_fibonacci = fibonacci(14)
print(f"The 14th Fibonacci number is: {nth_fibonacci}")
