pos= 0

def search(l,n):
    i = 0

    while i < len(l):
        if l[i] == n:
            globals() ['pos'] = i
            return True
        i = i + 1

    return False

l=[5,8,4,6,9,2]
n=9

if search(l,n):
    print("Found at", pos+1)
else:
    print("Not Found")
