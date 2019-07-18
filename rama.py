manu=input()
prashu=len(manu)
vgr="".join(manu[k:k+2][::-1] for k in range (0,prashu,2))
print (vgr)
