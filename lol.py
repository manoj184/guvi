manu,prashu=map(str,input().split())
for y in range(len(manu)):
    if(manu.count(manu[y])==prashu.count(prashu[y])):
        print("yes")
        break
    else:
        print("no")
        break
