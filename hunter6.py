n=int(input())
l=input().split()
count=0
dic=dict()
for i in range(0,len(l)):
    count=0
    for j in range(i+1,len(l)):
        count=count+1
        if(l[i]==l[j]):
            dic.update({l[i]:count})
            #print(l[i],count)
            break
if(len(dic)==0):
    print("unique")
else:
    print(min(dic,key=dic.get))      
   
