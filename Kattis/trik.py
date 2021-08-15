def A(a):
    k=a[0]
    a[0]=a[1]
    a[1]=k
    return a
    
def B(a):
    k=a[1]
    a[1]=a[2]
    a[2]=k 
    return a
    
def C(a):
    k=a[0]
    a[0]=a[2]
    a[2]=k 
    return a
    
m=input()
n=len(m)
a=[1,2,3]
for i in range(n):
    if m[i]=='A':
        a=A(a)
    if  m[i]=='B':
        a=B(a)
    if  m[i]=='C':
        a=C(a)
    i+=1
position=a.index(1)+1
print(position)