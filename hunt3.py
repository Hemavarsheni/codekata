num=int(input(""))
l=list(map(int,input("").split()))
m=[]
for i in range(len(l)):
    if(l[i]==i):
        m.append(l[i])
m.sort()
for i in m:
    print(i,end=" ")
