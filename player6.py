n=str(input())
k=str(input())
count=0
list1=[]
list2=[]
for i in n:
    list1.append(n.count(i))
for i in k:
    list2.append(k.count(i))
if(list1==list2):
    print("yes")
else:
    print("no")
