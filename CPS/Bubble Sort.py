#Bubble Sort

def B_Sort(array,size):
    for i in range(size-1):
        T=False
        for j in range(size-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                T=True
        if not T:
            break

l=[5,2,1,4,3,2,9,1,32,7,6]
B_Sort(l,len(l))
print(l)
