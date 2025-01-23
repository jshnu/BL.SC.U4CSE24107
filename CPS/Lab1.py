#Question 1
n=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))
print("Additon of",n,"+",m,"=",n+m)
print("Subtraction of",n,"-",m,"=",n-m)
print("Multiplication of",n,"x",m,"=",n*m)
print("Division of",n,"÷",m,"=",n/m)
print()

#Question 2
n=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))
o=int(input("Enter the third number: "))
print("Addition of",n,"+",m,"+",o,":",n+m+o)
print()

#Question 3
s=float(input("Enter the square's side length (in cm): "))
print("Area of square of side length",str(s)+"cm :",str(s*s)+"cm^2")
print()

#Question 4
l=float(input("Enter the rectange's length (in cm): "))
b=float(input("Enter the rectange's breadth (in cm): "))
print("Area of rectange with length",str(l)+"cm and breadth",str(b)+"cm :",str(l*b)+"cm^2")
print()

#Question 5
r=float(input("Enter the radius of the circle (in cm): "))
area=3.14159*(r**2)
print("Area of circle with radius",str(r)+"cm :",str(area)+"cm^2")
print()

#Question 6
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
D=b**2 - 4*a*c
print("The Discriminant b^2 - 4ac :",D)
print()

#Question 7
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
result=((a+b)**0.5)/2
print("The result of √(a+b)/2 :",result)
print()
