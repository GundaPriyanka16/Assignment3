"Write a program in python to check whether a number is palindrome or not using recursive method."

def is_palindrome(n): 
    n_str = str(n) 
    return n_str == n_str[::-1] 

n = 54321
if is_palindrome(n): 
    print("Palindrome") 
else: 
    print("Not a Palindrome")