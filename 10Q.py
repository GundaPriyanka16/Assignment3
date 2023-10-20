"Write a program in python to find sum of digits of a number using recursion." 

def sum_of_digits(n): 
    if n < 10 : 
        return n 
    return (n % 10 + sum_of_digits(n // 10)) 

n = 12345
result = sum_of_digits(n) 
print(result)