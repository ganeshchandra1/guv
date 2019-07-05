import math
n=int(input())
a=n
list1=[]
while n % 2 == 0: 
    print(2,end=' ') 
    n = n / 2
        
for i in range(3, int(math.sqrt(n))+1, 2): 
    
    while n % i == 0: 
        if i not in list1:
             list1.append(i)
             n=n/i
             print(','.join(map(str, list1)))
if n > 2: 
    print(n) 
