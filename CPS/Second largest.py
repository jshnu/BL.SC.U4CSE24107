"""Finding the Second Largest Number: Given three distinct numbers, write a Python program to find the second largest number
using only if-else statements."""

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a==b or b==c:
    print(f"Two of the numbers are equal. The second greatest number is: {b}")
if a==c:
    print(f"Two of the numbers are equal. The second greatest number is: {c}")
elif a>b>c:
    print(f"The second greatest number is: {b}")
elif a>c>b:
    print(f"The second greatest number is: {c}")
elif c>a>b:
    print(f"The second greatest number is: {a}")
elif c>b>a:
    print(f"The second greatest number is: {b}")
elif b>a>c:
    print(f"The second greatest number is: {a}")
elif b>c>a:
    print(f"The second greatest number is: {c}")
