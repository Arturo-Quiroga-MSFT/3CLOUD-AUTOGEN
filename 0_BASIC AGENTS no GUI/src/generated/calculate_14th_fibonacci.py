# filename: calculate_14th_fibonacci.py
def calculate_fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n):
        prev, curr = curr, prev + curr
    return curr

# Calculate the 14th Fibonacci number
n = 14
fibonacci_14 = calculate_fibonacci(n)
print(f"The 14th Fibonacci number is: {fibonacci_14}")
