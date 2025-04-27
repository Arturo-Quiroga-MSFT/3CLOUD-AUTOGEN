# filename: fibonacci_calculator.py

def fibonacci(n):
    if n <= 0:
        return "Invalid input! Fibonacci sequence starts from n=1."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Loop to calculate Fibonacci numbers up to n
    for _ in range(2, n):
        a, b = b, a + b
    
    return b

# Calculate the 14th Fibonacci number
result = fibonacci(14)
print(f"The 14th Fibonacci number is: {result}")
