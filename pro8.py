n=int(input())
k=input().split()
li=[]
l2=[]
for i in range(0,len(k)):
    for j in range(i+1,len(k)):
        for l in range(j+1,len(k)):
            if(i<j<l):
                if(int(k[i])<int(k[j])<int(k[l])):
                    li.append(k[i]+k[j]+k[l])
for i in li:
    if i not in l2:
        l2.append(i)
print(len(l2))
        
