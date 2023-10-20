"Write a program in python to check whether an integer is Armstrong number or not." 

n = int(371) 
n_str = str(n) 
a = int(n_str[0]) 
b = int(n_str[1]) 
c = int(n_str[2])
d = (a**3) + (b**3) + (c **3)
if n == d : 
    print("True") 
else: 
    print("False")