#Insertion Sort:

def I_Sort(array,size):
    if size <= 1:
        return
    
    for i in range(1,size):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key


arr = [12, 11, 13, 5, 6]
I_Sort(arr,len(arr))
print(arr)


#Insertion Sort: Recursion

def I2_Sort(array,n,size):
    if size <= 1:
        return
    if n==size:
        return
    
    key=array[n]
    j=n-1
    while j>=0 and key<array[j]:
        array[j+1]=array[j]
        j-=1
    array[j+1]=key
    return I2_Sort(array,n+1,size)


arr = [12, 11, 13, 5, 6]
I2_Sort(arr,1,len(arr))
print(arr)
