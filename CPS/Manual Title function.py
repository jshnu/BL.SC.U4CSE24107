# Converting String To Title Case without the use of the in-built functiion title()

a=input("Enter a string:")
s=a[0].upper()
for i in range(1,len(a)):
    if a[i-1]==" ":
        s+=a[i].upper()
    else:
        s+=a[i]
print(s)
