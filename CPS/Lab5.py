n=int(input("Enter the number of rows: "))


#Regular Pyramid
print("Regular Pyramid")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
print()

#Inverted Pyramid
print("Inverted Pyramid")
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))
print()

#Right Aligned Pyramid
print("Right Aligned Pyramid")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(i))
print()

#Left Aligned Pyramid
print("Left Aligned Pyramid")
for i in range(1,n+1):
    print("*"*(i))
print()

#Square
print("Square")
for i in range(1,n+1):
    print("* "*n)
print()

#Rectangle
print("Rectangle")
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
for i in range(r):
    print("* "*c)
print()

#Rhombus
print("Rhombus")
for i in range(1,n+1):
    print("  "*(n-i)+"* "*n)
print()

#Square: Numbers
print("Square: Numbers")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
print()

#Rectangle: Numbers
print("Rectangle: Numbers")
for i in range(r):
    for j in range(1,c+1):
        print(j,end=" ")
    print()
print()

#Rhombus: Numbers
print("Rhombus: Numbers")
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,n+1):
        print(j,end=" ")
    print()
print()


#Regular Pyramid: Numbers
print("Regular Pyramid: Numbers")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

#Inverted Pyramid: Numbers
print("Inverted Pyramid: Numbers")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

#Centered Pyramid: Numbers
print("Centered Pyramid: Numbers")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
print()


#Full Pyramid: Same Numbers
print("Full Pyramid: Same Numbers")
a=1
for i in range(1,n*2,2):
    print(" "*(n*2-i),end="")
    for j in range(1,i+1):
        print(a,end=" ")
    print()
    a+=1
print()











