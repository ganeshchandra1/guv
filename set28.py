n=int(input())
k=int(input())
for i in range(n+1,k):
    temp=i
    sum=0
    while(i>0):
        rem=i%10
        sum=sum+rem*rem*rem
        i=i//10
    if(sum==temp):
       print(temp)
