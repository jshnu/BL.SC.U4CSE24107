n=int(input("Enter the number of terms in fibbonacci series:"))
a,b,i=0,1,1
while i<=n:
    print(a,  end=" ")
    a,b = b,a+b
    i=i+1
print()

# 3 - 6X + 9X^2 ...... + 3NX^N
n=int(input("Enter number N:"))
X=int(input("Enter X:"))
i=0
sum=0
while i<=n:
    sum=sum+((i+1)*3)*((-X)**i)
    i+=1
print(sum)
