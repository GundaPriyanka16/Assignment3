"Write a program in python to check given number is prime or not." 

n = int(10) 
is_prime = True 
for i in range(2,n): 
    if (n % i) == 0: 
        is_prime = False 
        break 
print(is_prime)