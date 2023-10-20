"Write a program in python to print the Fibonacci series using recursive method."

def fibonacci(n): 
    if n <= 1: 
        return n 
    return fibonacci(n-1) + fibonacci(n-2) 

n = int(8) 
result = fibonacci(n) 
print(result) 