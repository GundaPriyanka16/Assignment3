"Write a program in python to check if a number is binary."

def is_binary(n): 
    for digit in n: 
        if digit not in '01': 
            return False 
    return True 
n = input() 
if is_binary(n):
    print("Binary Number") 
else: 
    print("Not a Binary Number")