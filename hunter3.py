n=int(input())
list1=list(input().split())
for i in range(0,n):
    if(i==int(list1[i])):
        print(list1[i],end='')
else:
     print("-1")
