a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
N=max(a,b);D=min(a,b)
r=N%D
while r!=0:
    N=D
    D=r
    r=N%D
print(f"GCD is {D}")
print(f"LCM is {int((a*b)/D)}")
