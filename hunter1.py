k=int(input())
list1=[]
list2=[]
list1=list(input().split())
for i in range(0,len(list1)):
    if (list1.count(list1[i])>=2):
        list2.append(list1[i])
print(' '.join(sorted(set(list2))))
