#Question 1
n= float(input("Enter a number:"))
if n>=0:
    print("The Number is Positve")
else:
    print("The Number is Negative")

#Question 2
n= float(input("Enter a number:"))
if n>0:
    print("The Number is Positve")
elif n==0:
    print("The Number is Zero")
else:
    print("The Number is Negative")

#Question 3
n= float(input("Enter a number:"))
if n%2==0:
    print("The Number is Even")
else:
    print("The Number is Odd")

#Question 4
n=float(input("Enter your age:"))
if n>=18:
    print("You are Eligible for voting")
else:
    print("You are not eligible for voting")

#Question 5
a=float(input("Enter number 1:"))
b=float(input("Enter number 2:"))
c=float(input("Enter number 3:"))
print("The largest number is",max([a,b,c]))

#Question 6
phy=float(input("Enter your physics marks:"))
chem=float(input("Enter your chemistry marks:"))
math=float(input("Enter your math marks:"))
avg_marks=(phy+chem+math)/3
if avg_marks>80:
    print("You have A Grade")
elif avg_marks>60 and avg_marks<=80:
    print("You have B Grade")
elif avg_marks>40 and avg_marks<=60:
    print("You have C Grade")
else:
    print("You have F Grade")
    
#Question 7
points=0
while True:
    char=input("Enter a character:")
    if char.isdigit():
        break
    elif len(char)==1:
        break
    else:
        print()
        print("Please enter only 1 character!!")
        print()
    
if char in "aeiouAEIOU":
    points=5
elif char.isdigit():
    points=10
print("your points are",points)

#Question 8
while True:
    char=input("Enter a single letter:")
    if len(char)==1:
        break
    else:
        print()
        print("Please enter only 1 letter!!")
        print()

if char.islower():
    print("The letter is lowercase!")
elif char.isupper():
    print("The letter is uppercase!")
else:
    print("The input is not lowercase or uppercase!")
        
#Question 9
print("Considering a quadratic equation in the form of Ax^2 + Bx + C = 0")
A=float(input("Enter the coefficient A:"))
B=float(input("Enter the coefficient B:"))
C=float(input("Enter the coefficient C:"))
D=(B**2 - 4*A*C)
if D>0:
    print("The roots are Real! You get 20 points!!")
elif D==0:
    print("The roots are Real and Equal! You get 0 points!!")
else:
    print("The roots are Imaginary! You get 10 points!!")

#Question 10
while True:
    print("Which unit is your weight")
    w_type=input("Kilogram (kg)/ Pounds (lbs) :")
    w_type=w_type.lower()
    if w_type in ["kg","lbs"]:
        break
    else:
        print()
        print("## INVALID INPUT ##")
        print()
w=float(input("Please Enter Your Weight:"))
print()
if w_type=="lbs":
    w=w/2.205
while True:
    print("Which unit is your height")
    h_type=input("Meter (m)/Centimeter (cm)/feet (ft) :")
    h_type=h_type.lower()
    if h_type in ["m","cm","ft"]:
        break
    else:
        print()
        print("## INVALID INPUT ##")
        print()
h=float(input("Please Enter Your height:"))
print()
if h_type=="cm":
    h/=100
elif h_type=="ft":
    h/=3.281
bmi=w/(h**2)
if bmi>=25:
    print("BMI is",round(bmi,2))
    print("Person is Overweight")
elif 18.5<=bmi<25:
    print("BMI is",round(bmi,2))
    print("Person is Normal weight")
else:
    print("BMI is",round(bmi,2))
    print("Person is Underweight")

#Question 11
point=tuple(eval(input("Enter the coordinates of a point in the x-y plane (x,y):")))
if point[0]>0 and point[1]>0:
    print('The point is in the I Quadrant')
elif point[0]<0 and point[1]>0:
    print('The point is in the II Quadrant')
elif point[0]<0 and point[1]<0:
    print('The point is in the III Quadrant')
elif point[0]>0 and point[1]<0:
    print('The point is in the IV Quadrant')
else:
    if point[0]==0 and point[1]==0:
        print("The point is on the origin")
    elif point[0]==0:
        print("The point is on the y-axis")
    elif point[1]==0:
        print("The point is on the x-axis")

#Question 12
year = int(input("Enter the year:"))
leap = False
if year%4==0:
    if year%400==0:
        leap = True
    elif year%100==0:
        pass
    else:
        leap = True
if leap:
    print("It is a leap year!")
else:
    print("It is not a leap year!")

#Question 13
amt=float(input("Enter amount spent:"))
if amt<1000:
    print("5 % Discount Applied")
    print("Final Amount:",amt*0.95,"rs")
elif amt<5000:
    print("10 % Disount Applied")
    print("Final Amount:",amt*0.90,"rs")
elif amt<10000:
    print("20 % Discount Applied")
    print("Final Amount:",amt*0.80,"rs")
else:
    print("No Discount Applied")
    print("Final Amount:",amt,"rs")
