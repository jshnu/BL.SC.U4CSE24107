#Diamond
n=int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(i,n):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(i,n):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()

#Equal Diamond
n=int(input("Enter the number of rows:"))
a=1
for i in range(n):
    print("  "*(n - 1 - i),end="")
    for j in range(a):
        print("*",end=" ")
    print()
    a+=2
a-=4
for i in range(n-2,-1,-1):
    print("  "*(n - 1 - i),end="")
    for j in range(a):
        print("*",end=" ")
    a-=2
    print()

#Hollow Rectangle
n=int(input("Enter the number of rows:"))
m=int(input("Enter the number of columns:"))
for i in range(n):
    if i not in [0 , n-1]:
        for j in range(m):
            if j not in [0, m-1]:
                print(end="  ")
            else:
                print("*",end=" ")
                
        print()
    else:
        for j in range(m):
            print("*",end=" ")
        print()



