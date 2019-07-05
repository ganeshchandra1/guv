n=int(input())
list1=[]
count=0
str="kabali"
res=0
count1=len(str)
for i in range(n):
    list1.append(input())
for i in range(0,len(list1)):
    count=0
    for j in list1[i]:
        if j in str and list1[i].count(j)==str.count(j):
            count=count+1
    if(count==6):
        res=res+1
print(res)
