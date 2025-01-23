num=int(input("Enter a 4 digit integer:"))
if num<0:
    num=num*-1
num=str(num)
i=0;e_sum=0;o_sum=0
while i<len(num):
    if (i+1)%2==0:
        e_sum+=int(num[i])
    else:
        o_sum+=int(num[i])
    i+=1
print(f"Sum of Even digits: {e_sum} Sum of Odd digits: {o_sum}")
