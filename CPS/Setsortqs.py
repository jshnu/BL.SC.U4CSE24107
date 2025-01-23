"""Question:
You are given two lists of integers. Convert them into sets and find the elements that are common to both sets. Then, sort these common elements in ascending order and return the result.

Example Input:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

Expected Output:
[3, 4, 5]"""

def insert_sort(arr,size):
    if size<=1:
        return
    for i in range(1,size):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list1=set(list1)
list2=set(list2)
list3=list(list1&list2)
insert_sort(list3,len(list3))
print(list3)

