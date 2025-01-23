#Set A

#Question 1
def Transpose(X):
    X_T=[[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    return X_T

def Add(X,Y):
    Z=[[[] for j in X[0]] for i in X]
    for i in range(len(X)):
        for j in range(len(X[0])):
            Z[i][j]=X[i][j]+Y[i][j]
    return Z

A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[10,12,13],[14,15,16],[17,18,19]]

R1=Transpose(Add(A,B))
R2=Add(Transpose(A),Transpose(B))
if R1==R2:
    R="Satisfies (A+B)' = A'+B' "
else:
    R="Does Not Satify (A+B)' = A'+B'"
print(f"(A+B)' :", R1)
print(f"A'+B' :", R2)
print(R)
print()

#Question 2
n=5
for i in range(1,n*2,2):
    print(" "*(2*n-1-i)+"* "*i)
for i in range((n-1)*2-1,0,-2):
    print(" "*(2*n-1-i)+"* "*(i))
print()


#Question 3
def Sum(X,n,s=0):
    if n==len(X):
        return s
    else:
        return Sum(X,n+1,s+X[n])

l=[20,32,10,30,15]
print("Sum of elements: ",Sum(l,0))

