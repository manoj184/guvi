g=int(input())
e=2
w=1
while(e<g):
       if(g%e==0):
              w=0
              break
       else:
              e=e+1
if w==0:
       print('no')
else:
       print('yes')
