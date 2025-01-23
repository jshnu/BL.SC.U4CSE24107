"""Odd or Even without Modulus: Write a Python program to check if a number is odd or even
without using the modulus operator % or division operator /."""
num=int(input("Enter a number:"))
num=str(num)
if int(num[-1]) in [0,2,4,6,8]:
    print("Even")
else:
    print("Odd")
