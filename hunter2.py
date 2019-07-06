n=int(input())
list1=list(input().split())
list2=[]
while(len(list1)>0):
    list2.append(max(list1))
    list1.remove(max(list1))
print(''.join(list2))
