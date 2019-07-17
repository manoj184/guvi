p=int(input())
m=[]
a=[]
r=[]
h=[]
t=0
for i in range(0,p):
    d=input()
    m.append(d)
for i in m:
    for j in range(0,len(i)+1):
        a.append(i[:j])
for i in a:
    if i!='':
        h.append(i)
for i in h:
    r.append(a.count(i))
for i in range(0,len(r)):
    t=t+1
    if r[i]!=p:
        break
print(h[t-2])

