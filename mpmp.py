manu=input()
prashu=manu.split()
count=0
for k in range(0,len(prashu[0])):
    if prashu[0][k]!=prashu[1][k]:
        count=count+1
if (count==1):
    print("yes")
else:
    print("no")
