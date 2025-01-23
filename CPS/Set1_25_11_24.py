"""SET 1:
Take list as user input
Search the list and find the number of times the element is repeating
Recursively
"""
def Linear_Search_Count(X,z,n,count):
    if n==len(X):
        return count
    if X[n]==z:
        count+=1
    return Linear_Search_Count(X,z,n+1,count)
l=list(eval(input("Enter the list to be searched: ")))
x=int(input("Enter the element to be searched: "))
Num=Linear_Search_Count(l,x,0,0)
print(f"Number of occurences of element {x} in list is: ",Num)
