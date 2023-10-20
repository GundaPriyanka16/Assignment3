"Write a program in python to print the Fibonacci series using iterative method."

def fib_iterative(n): 
    series = [0,1] 
    while len(series) < n:
        a = series[-1] + series[-2] 
        series.append(a) 
    return series 
n = int(10) 
series = fib_iterative(n) 
print(series)