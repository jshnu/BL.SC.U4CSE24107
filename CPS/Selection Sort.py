#Selection Sort

def S_Sort(array,size):
    for i in range(size-1):
        _min=i
        for j in range(i+1,size):
            if array[j]<array[i]:
                _min=j
        array[i],array[_min]=array[_min],array[i]

l=[5,2,1,4,3,2,9,1,32,7,6]
S_Sort(l,len(l))
print(l)



##Selection Sort: Recursion

def S2_Sort(array,n,size):
    if n==size-1:
        return
    _min=n
    for j in range(n+1,size):
        if array[j]<array[n]:
            _min=j
    array[n],array[_min]=array[_min],array[n]
    return S2_Sort(array,n+1,size)

l=[5,2,1,4,3,2,9,1,32,7,6]
S2_Sort(l,0,len(l))
print(l)
