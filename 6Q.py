"Write a program in python to check whether a number is palindrome or not using iterative method."

n = int(123) 
a = n 
rev = 0
while a > 0:
    b = a % 10
    rev = (rev * 10) + b 
    a = a // 10
if n == rev: 
    print("Palindrome") 
else: 
    print("Not Palindrome")