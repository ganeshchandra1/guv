n=int(input())
list2=[]
list1=list(input().split())
for i in range(0,n):
    if(i==int(list1[i])):
        list2.append(i)
if(len(list2)==1):
    print("-1")
else:
    print(' '.join(map(str,list2)))
